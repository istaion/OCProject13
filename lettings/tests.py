from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingsTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('lettings_index'))
        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content

    def test_detail(self):
        address = Address.objects.create(
            number=7217,
            street='Bedford Street',
            city='Brunswick',
            state='GA',
            zip_code=31525,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(
            title='Joshua Tree Green Haus /w Hot Tub',
            address_id=address.id
        )
        response = self.client.get(reverse('letting', args=[letting.id]))
        assert response.status_code == 200
        assert b'<p>Brunswick, GA 31525</p>' in response.content
