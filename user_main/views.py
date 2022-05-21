from .models import Equip, EquipCode
from django.shortcuts import render, redirect
from django.http import HttpResponse
#



def user_main(request):
    
    
    return render(request, 'user_main.html')
