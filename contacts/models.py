from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):

    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.EmailField()
    phone = PhoneNumberField()