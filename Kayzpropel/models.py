from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.firstname+" "+self.lastname

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=150)
    upload_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Transactions(models.Model):
     amount = models.CharField(max_length=20)
     phone_number = models.CharField(max_length=20)
     transaction_date = models.DateField(default=timezone.now)


# class ImageModel(models.Model):
#     image = models.ImageField(upload_to='images/')
#     title = models.CharField(max_length=50)
#     price = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
# class Profile(models.Model):
#     username =