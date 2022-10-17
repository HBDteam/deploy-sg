from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from feat_user.user_main.models import Renting
from feat_admin.admin_main.models import Equip
from sign.models import User
import datetime
from time import gmtime, strftime
from pytz import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


def adminMain(request):
    date = datetime.datetime.today()
    rentings = Renting.objects.filter(rentingDate=date)
    returnings = Renting.objects.filter(returningDate=date)
    context = {'rentings': rentings, 'returnings': returnings}
    return render(request, 'admin_main.html', context)

def renting(request):
    if request.method == 'GET':
        # now_date = datetime.datetime.now(timezone("Asia/Seoul")) - datetime.timedelta(days=7) # 오늘 날짜를 가져온다. (test: 7일전)
        user_history_query = Renting.objects.filter().only('userName','equipID_no', 'rentingDate', 'returningDate') # Renting 테이블에서 원하는 컬럼만 가져온다.
        rent_user_list = []
        rent_list = []
        for data in user_history_query:
            # if data.rentingDate.strftime("%Y-%m-%d") >= now_date.strftime("%Y-%m-%d") : # 오늘 날짜 이후인 것만 보여준다.
            rent_user_list.append(data)
        for data in rent_user_list:
            equip_query = Equip.objects.filter(equipID=data.equipID_no)
            if equip_query:
                rent_list.append(data)
                if str(data.equipID_no) == str(equip_query[0].equipID):
                    data.equipInfo = equip_query[0].equipInfo
        context = {'rent_user_list' : rent_list }
        return render(request, 'admin_equipment_rental.html', context)
    # return render(request, 'admin_equipment_rental.html')

@csrf_exempt
def rent_detail_ajax(request):
    if request.method == 'POST':
        select_equipID = request.POST.get('select_equipID')
        select_userName = request.POST.get('select_userName')
        select_rentingDate = request.POST.get('select_rentingDate')
        select_returningDate = request.POST.get('select_returningDate')
        user_rented_query = Renting.objects.get(userName=select_userName,equipID_no=select_equipID) #유저이름과 장비코드를 사용해 유저 아이디를 찾는다.
        select_equipID = user_rented_query.userID_no
        user_detail_query = User.objects.get(studentID__contains=select_equipID)
        print(user_detail_query)
        studentID = user_detail_query.studentID
        studentName = user_detail_query.name
        studentEmail = user_detail_query.email
        studentPhonenum = user_detail_query.phoneNum
        Equip_q = Equip.objects.all()
        print(Equip_q.values())

        return JsonResponse({'studentID': studentID, 'studentName':studentName, 'studentEmail':studentEmail, 'studentPhonenum':studentPhonenum })