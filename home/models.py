from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField() 

    def __str__(self):
        return self.name
    



class Hotel(models.Model):
    name = models.CharField(max_length=122)
    destination = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    


class Ticket(models.Model):
    name = models.CharField(max_length=122)
    destination = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
     
