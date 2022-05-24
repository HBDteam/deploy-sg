from csv import register_dialect
from django.db import models
from sign.models import *
from admin_main.models import *

# Create your models here.


class Lab(models.Model):
    labNum = models.IntegerField(primary_key=True, null=False)
    manager = models.CharField(max_length=10, null=False)
    mPhoneNum = models.CharField(max_length=11, null=False)
    curPeople = models.IntegerField(null=False)


class Renting(models.Model):
    serialnum = models.IntegerField(primary_key=True, null=False)
    equipID = models.ForeignKey(Equip, on_delete=models.PROTECT, null=True)
    userName = models.CharField(max_length=10, null=True)
    userID = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    userPhoneNum = models.CharField(max_length=11, null=True)
    rentingDate = models.DateField(null=True)
    returningDate = models.DateField(null=True)

    def __str__(self):
        return f'[{self.serialnum}]'
