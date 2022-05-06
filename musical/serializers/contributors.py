from rest_framework import serializers

from musical.models import Contributors


class ContributorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributors
        fields = ['name']
