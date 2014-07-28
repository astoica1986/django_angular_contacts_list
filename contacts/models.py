from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):

    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.EmailField()
    phone = PhoneNumberField()