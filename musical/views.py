from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from musical.models import MusicalWork, MusicalContributors, Contributors
from musical.serializers.contributors import ContributorsSerializer
from musical.serializers.musical_contributors import MusicalContributorsSerializer
from musical.serializers.musical_work import MusicalWorkSerializer


class MusicalWorkViewSet(viewsets.ModelViewSet):
    queryset = MusicalWork.objects.all()
    serializer_class = MusicalWorkSerializer

    def get_queryset(self):
        """
        Showing all musical works unless there is a iswc provided
        """
        iswc = self.request.query_params.get("iswc", None)

        if iswc:
            queryset = MusicalWork.objects.filter(iswc=iswc)
            return queryset

        return super().get_queryset()


class MusicalContributorsViewSet(viewsets.ModelViewSet):
    queryset = MusicalContributors.objects.all()
    serializer_class = MusicalContributorsSerializer


class ContributorsViewSet(viewsets.ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
