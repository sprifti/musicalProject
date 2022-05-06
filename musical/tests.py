from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from musical.models import MusicalWork
from musical.serializers.musical_work import MusicalWorkSerializer
from musical.views import MusicalWorkViewSet


class ViewsTestCase(TestCase):
    def test_single_view_loads_properly(self):
        response = self.client.get('https://0.0.0.0:8000')
        self.assertEqual(response.status_code, 200)
