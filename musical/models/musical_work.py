from django.db import models

from musical.models.contributors import Contributors


class MusicalWork(models.Model):
    iswc = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    contributors = models.ManyToManyField(Contributors, through='MusicalContributors')
