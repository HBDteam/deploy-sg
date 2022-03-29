from statistics import mode
from django.db import models
from user_main.models import *
from sign.models import *

# 장비 코드(카테고리) 테이블


class EquipCode(models.Model):
    equipCode = models.IntegerField(primary_key=True, null=False)
    equipName = models.CharField(max_length=20, null=False)


# 각 장비의 정보 테이블


class Equip(models.Model):
    euipCode = models.ForeignKey(EquipCode, on_delete=models.DO_NOTHING)
    equipID = models.CharField(primary_key=True, max_length=10, null=False)
    receivedDate = models.DateField(default='')
    isRented = models.PositiveSmallIntegerField(null=False)
    status = models.PositiveSmallIntegerField(null=False)
    equipInfo = models.TextField(default='')
