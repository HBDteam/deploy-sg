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

def renting(request):
    if request.method == 'GET':
        now_date = datetime.today() # 오늘 날짜를 가져온다.
        user_history_query = Renting.objects.filter().only('userName','equipID', 'rentingDate', 'returningDate') # Renting 테이블에서 원하는 컬럼만 가져온다.
        user_history_list = list(user_history_query) # 리스트로 변환한다.
        rent_user_list = []
        for data in user_history_list:
            if data['rentingDate'] >= now_date: # 오늘 날짜 이후인 것만 보여준다.
                rent_user_list.append(data)
        for data in rent_user_list:
            equip_query = Equip.objects.filter(equipID__in=data['equipID'])
            equip_query_list = list(equip_query) # 리스트로 변환한다.
            for i in range(len(equip_query_list)):
                rent_user_list[i]['equipInfo'] = equip_query_list[i]['equipInfo']
        print(rent_user_list)
        context = {'rent_user_list' : rent_user_list }
        return render(request, 'admin_equipment_rental.html', context)
    # return render(request, 'admin_equipment_rental.html')