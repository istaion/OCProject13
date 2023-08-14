from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class to represent an app's user.

    ...

    Attributes
    ----------
    user : user object
    favorite_city : str
        favorite city of the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
