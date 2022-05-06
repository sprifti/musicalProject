from django.db import models

from musical.models.contributors import Contributors
from musical.models.musical_work import MusicalWork


class MusicalContributors(models.Model):
    musical_work = models.ForeignKey(MusicalWork, on_delete=models.CASCADE)
    contributors = models.ForeignKey(Contributors, on_delete=models.CASCADE)
