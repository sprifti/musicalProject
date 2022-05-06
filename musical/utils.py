from musical.models import Contributors


def insert_contributors(contributors_df):
    batch_size = 100
    contributors = []
    for name in contributors_df["contributors"].unique():
        if not Contributors.objects.filter(name=name).exists():
            contributors.append(Contributors(name=name))
    try:
        Contributors.objects.bulk_create(contributors, batch_size=batch_size)
        return True
    except Exception as e:
        return False
