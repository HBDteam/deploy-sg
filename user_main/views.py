from .models import Equip, EquipCode, User, Renting
from django.shortcuts import render, redirect
from django.http import HttpResponse

#



def user_main(request):

    Users = User.objects.filter(studentID="20190811")


    NOW_userID = Renting.objects.filter(userID="20190811")
    equipid = NOW_userID.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    NOW_userID_list = list(NOW_userID.values())
    equip_list = list(equip.values('equipInfo'))
    print(len(equip_list))
    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']

    

    context = {'Users' : Users, 'NOW_userID_list' : NOW_userID_list}

    
    return render(request, 'user_main.html', context)
