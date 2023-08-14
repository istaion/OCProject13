from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A class to represent a address.

    ...

    Attributes
    ----------
    number : int
        number of the address
    street : str
        name of the street
    city : str
        city of the address
    state : str
        state of the address
    zip_code : int
        Zone Improvement Plan
    country_iso_code : int
        International Standard for country codes
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    A class to represent a letting.

    ...

    Attributes
    ----------
    title : str
        name of the letting
    address : address model
        address of the letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
