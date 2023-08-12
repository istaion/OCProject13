from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfilesTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('profiles_index'))
        assert response.status_code == 200
        assert b'<title>Profiles</title>' in response.content

    def test_detail(self):
        user = User.objects.create_user(username='testuser',
                                        first_name='Rebecca',
                                        last_name='Warrior',
                                        email='rebecca@warrior.com')
        profile = Profile.objects.create(
            user=user,
            favorite_city='Lille'
        )

        response = self.client.get(reverse('profile', args=[profile.user.username]))
        assert response.status_code == 200
        assert b'<p>Email: rebecca@warrior.com</p>' in response.content
