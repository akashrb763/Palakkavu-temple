from django.db import models
from django.urls import reverse


# Create your models here.
class Notifications(models.Model):
    titel = models.CharField(max_length=80)
    notify = models.CharField(max_length=500)

    def __str__(self):
        return '{}'.format(self.titel)


class Feeds(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='Feeds', blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class PoojaTime(models.Model):
    pooja_name = models.CharField(max_length=250)
    poojatime_from = models.TimeField()
    poojatime_to = models.TimeField()

    def __str__(self):
        return '{}'.format(self.pooja_name)


class AnnounceMent(models.Model):
    annos_name = models.CharField(max_length=80)
    annosmt = models.CharField(max_length=400)

    def __str__(self):
        return '{}'.format(self.annos_name)



class spcilepooja(models.Model):
    pooja_name = models.CharField(max_length=80)
    sponser = models.CharField(max_length=100)
    sponser_addres=models.CharField(max_length=300)
    pooja_time=models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.pooja_name)


class Enquiry(models.Model):
    name=models.CharField(max_length=30)
    mobile_no=models.IntegerField(blank=True,null=True,max_length=10)
    qury=models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

# class Donation(models.Model):
#     fullname=models.CharField(max_length=50)
#     Address=models.CharField(max_length=150)
#     MobileNo=models.IntegerField()
#     donation=models.Choices()





