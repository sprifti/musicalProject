from rest_framework import serializers

from musical.models import MusicalWork
from musical.serializers.contributors import ContributorsSerializer
from musical.serializers.musical_contributors import MusicalContributorsSerializer


class MusicalWorkSerializer(serializers.HyperlinkedModelSerializer):
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = MusicalWork
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["contributors"] = ContributorsSerializer(instance.contributors.all(), many=True,
                                                     context={'request': None}).data
        return rep
