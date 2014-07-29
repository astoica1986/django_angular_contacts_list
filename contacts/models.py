from django.db import models


class Contact(models.Model):

    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def as_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "phone": self.phone,
            "email": self.email
        }