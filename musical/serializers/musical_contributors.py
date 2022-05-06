from rest_framework import serializers

from musical.models import MusicalContributors


class MusicalContributorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicalContributors
        fields = '__all__'
