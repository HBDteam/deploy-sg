from .models import Equip, EquipCode
from django.shortcuts import render, redirect
from django.http import HttpResponse

import operator

def equipinfo(request):
    notebooks = Equip.objects.filter(equipCode=0) #노트북
    cables = Equip.objects.filter(equipCode=1) #케이블
    cdroms = Equip.objects.filter(equipCode=2) #CD롬
    arduinos = Equip.objects.filter(equipCode=3) #아두이노 키트
    raspberrypis = Equip.objects.filter(equipCode=4) #라즈베리파이
    jols = Equip.objects.filter(equipCode=5) #졸업작품 물품
    labs = Equip.objects.filter(equipCode=6) #실습실
    tabletpcs = Equip.objects.filter(equipCode=7) #태블릿 PC
    webcams = Equip.objects.filter(equipCode=8) #웹캠
    tablets = Equip.objects.filter(equipCode=9) #태블릿

    

   
    context = {'notebooks': notebooks, 'cables': cables, 'cdroms': cdroms, 'arduinos': arduinos, 'raspberrypis': raspberrypis, 'jols': jols, 'labs': labs, 'tabletpcs': tabletpcs, 'webcams': webcams, 'tablets': tablets}
    
    
    return render(request, 'user_equipment.html', context)
