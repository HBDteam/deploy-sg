from email.encoders import encode_quopri
from tkinter import W

from admin_main.models import EquipCode
from user_equipment.views import equipinfo
from .models import User, Renting, Equip
from django.shortcuts import render, redirect
from django.http import HttpResponse
#



def user_history(request):
    
    NOW_userID = Renting.objects.filter(userID="20190809")
    equipid = NOW_userID.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    NOW_userID_list = list(NOW_userID.values())
    equip_list = list(equip.values('equipInfo'))
    print(len(equip_list))
    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']

    print(NOW_userID_list)

    
    

    context = {'NOW_userID' : NOW_userID_list }
    
    return render(request, 'user_history.html', context)
