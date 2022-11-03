from email.encoders import encode_quopri
from tkinter import W

from feat_admin.admin_main.models import EquipCode
from feat_user.user_equipment.views import equipinfo
from .models import User, Renting, Equip
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from operator import itemgetter



def user_history(request):
    
    login_user_ID = request.user.username

    now = datetime.datetime.today()
    
    NOW_userID = Renting.objects.filter(userID = login_user_ID)

    equipid = NOW_userID.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    NOW_userID_list = list(NOW_userID.values())
    equip_list = list(equip.values('equipInfo'))

    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']

    
    NOW_userID_list.sort(key=itemgetter('returningDate'))

    now_list = NOW_userID_list[3:]
    past_list = NOW_userID_list[0:3]

    

    context = {'now_list' : now_list, 'past_list' : past_list}
    
    

   
    
    return render(request, 'user_history.html', context)

'''
    now_rentlist = []
    pre_rentlist = []


    

    for i in range(len(NOW_userID_list)):
        if NOW_userID_list[i]['returningDate'].strftime('%Y%m%d') > now:
            now_rentlist.append(NOW_userID_list[i])
        else:
            pre_rentlist.append(NOW_userID_list[i])

    now_rentlist.sort(key=itemgetter('returningDate'))
    pre_rentlist.sort(key=itemgetter('returningDate'))
    '''
    
    
