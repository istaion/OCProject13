from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        assert b'Welcome to Holiday Homes' in response.content
