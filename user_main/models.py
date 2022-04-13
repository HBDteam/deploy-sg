from csv import register_dialect
from django.db import models
from sign.models import *
from admin_main.models import Equip, EquipCode


class Lab(models.Model):
    labNum = models.IntegerField(primary_key=True, null = False)
    manager = models.CharField(max_length=10, null=False)
    mPhoneNum = models.CharField(max_length=11, null=False)
    curPeople = models.IntegerField(null=False)

class Renting(models.Model):
    serialnum = models.IntegerField(primary_key=True, null = False)
    equipID = models.ForeignKey(Equip, on_delete=models.PROTECT, null = False)
    userName = models.CharField(max_length=10, null=False)
    userID = models.ForeignKey(User, on_delete=models.PROTECT, null = False)
    userPhoneNum = models.CharField(max_length=11, null=False)
    rentingDate = models.DateField(null=False)
    returningDate = models.DateField(null=False)