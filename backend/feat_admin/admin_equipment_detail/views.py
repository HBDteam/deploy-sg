from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Equip, EquipCode

# Create your views here.


def adminEquipDetail(request):
    if request.method == 'GET':
        equipcode = request.GET.get('equipCode')
        if equipcode is None:
            equips = equips = Equip.objects.all()
        else:
            equips = Equip.objects.filter(equipCode=equipcode)
        context = {'equips': equips}
        return render(request, 'admin_equipment_detail.html', context)
    elif request.method == 'POST':
        equips = Equip.objects.all()
        context = {'equips': equips}
        return render(request, 'admin_equipment_detail.html', context)
