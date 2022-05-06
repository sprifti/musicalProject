import numpy as np
from django.core.management.base import BaseCommand, CommandError
from musical.models import *
import pandas as pd

from musical.utils import insert_contributors


class Command(BaseCommand):

    def handle(self, *args, **options):
        dataset = pd.read_csv("musical/data/works_metadata.csv")
        # Explode contributors to create a record for each combination
        dataset["contributors"] = dataset["contributors"].str.split("|")
        dataset = dataset.explode("contributors", ignore_index=False)

        # Combine title and contributors in case of Null iswc
        dataset["title_cont"] = dataset["title"] + "/" + dataset["contributors"]
        batch_size = 100
        # Insert contributors
        contributors = insert_contributors(dataset)

        musical_contributors = []
        processed_iswc = []

        if contributors:
            for index, row in dataset.iterrows():

                iswc = row["iswc"]
                title = row["title"]
                title_cont = row["title_cont"]

                if iswc is np.nan:
                    try:
                        # Use combination of title and contributor to get the missing iswc
                        iswc = \
                            dataset.loc[(dataset.title_cont == title_cont) & (dataset.iswc.notnull())]['iswc'].values[0]
                    except:
                        # In case the combination is not found anywhere else on the dataset the title is enough
                        # to identify the musical work
                        iswc = dataset.loc[(dataset.title == title) & (dataset.iswc.notnull())]['iswc'].values[0]

                # Check if musical work does not exist
                if not MusicalWork.objects.filter(iswc=iswc, title=title).exists() and iswc not in processed_iswc:
                    # Create musical_work to later use in MusicalContribution
                    MusicalWork(iswc=iswc, title=title).save()

                    processed_iswc.append(iswc)

                # Check if musical_contributors exists
                if not MusicalContributors.objects.filter(musical_work__iswc=iswc,
                                                          contributors__name=row["contributors"]).exists():
                    # Append to bulk insert
                    musical_contributors.append(
                        MusicalContributors(musical_work=MusicalWork.objects.get(iswc=iswc),
                                            contributors=Contributors.objects.get(name=row["contributors"])))
            try:
                MusicalContributors.objects.bulk_create(musical_contributors, batch_size=batch_size)
                # from django.core.mail import send_mail
                #
                # send_mail(
                #     'Subject here',
                #     'Data Ingestion finished successfully',
                #     'serenaprifti5@gmail.com',
                #     ['serenaprifti5@gmail.com'],
                #     fail_silently=False,
                # )
            except:
                print("An error occurred")
                # from django.core.mail import send_mail
                #
                # send_mail(
                #     'Subject here',
                #     'There has been an error!',
                #     'serenaprifti5@gmail.com',
                #     ['serenaprifti5@gmail.com'],
                #     fail_silently=False,
                # )
