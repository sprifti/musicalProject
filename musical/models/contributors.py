from django.db import models


class Contributors(models.Model):
    name = models.CharField(max_length=255)