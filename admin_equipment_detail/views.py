from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Equip, EquipCode

# Create your views here.


def adminEquipDetail(request):
    equips = Equip.objects.all()
    context = {'equips': equips}
    return render(request, 'admin_equipment_detail.html', context)
