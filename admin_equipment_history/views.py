from django.shortcuts import render
from user_main.models import Renting
import datetime

# Create your views here.


def adminHistory(request):
    date = datetime.datetime.today()
    isRentings = Renting.objects.filter(
        rentingDate__lte=date, returningDate__gt=date)
    isReturneds = Renting.objects.filter(returningDate__lt=date)
    context = {'isRentings': isRentings, 'isReturneds': isReturneds}
    return render(request, 'admin_history.html', context)
