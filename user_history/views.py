from email.encoders import encode_quopri

from admin_main.models import EquipCode
from user_equipment.views import equipinfo
from .models import User, Renting, Equip
from django.shortcuts import render, redirect
from django.http import HttpResponse
#



def user_history(request):
    
    NOW_userID = Renting.objects.filter(userID="20190811")
   

    context = {'NOW_userID' : NOW_userID}
    
    
    return render(request, 'user_history.html', context)
