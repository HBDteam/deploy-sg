from email.encoders import encode_quopri
from tkinter import W

from admin_main.models import EquipCode
from user_equipment.views import equipinfo
from .models import User, Renting, Equip
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime



def user_history(request):
    
    '''userid = Renting.objects.filter(userID="20190811")
    equipid = userid.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    equip_list = list(equip.values('equipInfo'))
    



    returningdate = userid.values('returningDate')
    

    print(returningdate)
    print(now)
    c=0
    c2=0
    for i in returningdate:
        if returningdate[i] <= now:
            c = c+1
            #PAST_userID_list = list(userid.values())
        else:
            c2 = c2+1
            #NOW_userID_list = list(userid.values())


    print(c)
    print(c2)
    
   
    for i in range(len(equip_list)):
        PAST_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']

    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']


     context = {'NOW_userID_list' : NOW_userID_list, 'PAST_userID_list' : PAST_userID_list }
    '''

    NOW_userID = Renting.objects.filter(userID="20190811")
    equipid = NOW_userID.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    NOW_userID_list = list(NOW_userID.values())
    equip_list = list(equip.values('equipInfo'))
    print(len(equip_list))
    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']


    print(NOW_userID_list)

    now = int(datetime.today().strftime('%Y%m%d'))
    
    
    context = {'NOW_userID_list' : NOW_userID_list , 'now' : now}
    
    

   
    
    return render(request, 'user_history.html', context)
