from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from user_main.models import Renting
from datetime import datetime
# Create your views here.


def adminMain(request):
    date = datetime.today()
    rentings = Renting.objects.filter(rentingDate=date)
    returnings = Renting.objects.filter(returningDate=date)
    context = {'rentings': rentings, 'returnings': returnings}
    return render(request, 'admin_main.html', context)
