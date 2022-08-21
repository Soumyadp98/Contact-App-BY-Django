from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    relationship= models.CharField(max_length=100)
    email=models.CharField( max_length=100)
    phone_no=models.CharField(max_length=20)
    address=models.CharField(max_length=500)


    def __str__(self):
        return self.full_name
