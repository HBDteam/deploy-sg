from calendar import c
from multiprocessing.sharedctypes import Value
from tkinter import W
from .models import Equip, EquipCode, User, Renting
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime


def user_main(request):

    Users = User.objects.filter(studentID="20190811")


    NOW_userID = Renting.objects.filter(userID="20190811")
    equipid = NOW_userID.values('equipID')
    equip = Equip.objects.filter(equipID__in=equipid)
    NOW_userID_list = list(NOW_userID.values())
    equip_list = list(equip.values('equipInfo'))

    equip_code0 = Equip.objects.filter(equipCode=0) #노트북
    equip_code1 = Equip.objects.filter(equipCode=1) #케이블
    equip_code2 = Equip.objects.filter(equipCode=2) #cdrom
    equip_code3 = Equip.objects.filter(equipCode=3) #아두이노
    equip_code4 = Equip.objects.filter(equipCode=4) #라즈베리파이
    equip_code5 = Equip.objects.filter(equipCode=5) #졸작물품
    equip_code6 = Equip.objects.filter(equipCode=6) #실습실
    equip_code7 = Equip.objects.filter(equipCode=7) #태블릿pc
    equip_code8 = Equip.objects.filter(equipCode=8) #웹캠
    equip_code9 = Equip.objects.filter(equipCode=9) #태블릿




    #equipCode_id별 isRented==0인 카운트 (재고량)
    
    code0_c = 0
    code0 =[]

    for i in range(len(equip_code0)):
        code0 = equip_code0.filter(isRented=0)
    
    for i in range(len(code0)):
        code0_c += 1

    print(code0_c)

    #########################################################

    code1_c = 0
    code1 =[]

    for i in range(len(equip_code1)):
        code1 = equip_code1.filter(isRented=0)
    
    for i in range(len(code1)):
        code1_c += 1

    print(code1_c)

    #########################################################

    code2_c = 0
    code2 =[]

    for i in range(len(equip_code2)):
        code2 = equip_code2.filter(isRented=0)
    
    for i in range(len(code2)):
        code2_c += 1

    print(code2_c)

    #########################################################

    code3_c = 0
    code3 =[]

    for i in range(len(equip_code3)):
        code3 = equip_code3.filter(isRented=0)
    
    for i in range(len(code3)):
        code3_c += 1

    print(code3_c)

    #########################################################

    code4_c = 0
    code4 =[]

    for i in range(len(equip_code4)):
        code4 = equip_code4.filter(isRented=0)
    
    for i in range(len(code4)):
        code4_c += 1

    print(code4_c)

    #########################################################

    code5_c = 0
    code5 =[]

    for i in range(len(equip_code5)):
        code5 = equip_code5.filter(isRented=0)
    
    for i in range(len(code5)):
        code5_c += 1

    print(code5_c)

    #########################################################

    code6_c = 0
    code6 =[]

    for i in range(len(equip_code6)):
        code6 = equip_code6.filter(isRented=0)
    
    for i in range(len(code6)):
        code6_c += 1

    print(code6_c)

    #########################################################

    code7_c = 0
    code7 =[]

    for i in range(len(equip_code7)):
        code7 = equip_code7.filter(isRented=0)
    
    for i in range(len(code7)):
        code7_c += 1

    print(code7_c)

    #########################################################

    code8_c = 0
    code8 =[]

    for i in range(len(equip_code8)):
        code8 = equip_code8.filter(isRented=0)
    
    for i in range(len(code8)):
        code8_c += 1

    print(code8_c)

    #########################################################

    code9_c = 0
    code9 =[]

    for i in range(len(equip_code9)):
        code9 = equip_code9.filter(isRented=0)
    
    for i in range(len(code9)):
        code9_c += 1

    print(code9_c)

    #########################################################

    #재고량순으로 인기 카테고리 적용(내림차순)
    goods = [['노트북', code0_c], ['케이블', code1_c], ['CD-ROM', code2_c], ['아두이노 키트', code3_c], ['라즈베리파이', code4_c], ['졸업작품 물품', code5_c], ['실습실', code6_c], ['태블릿PC', code7_c], ['웹캠', code8_c], ['태블릿', code9_c]]
    goods.sort(key=lambda x:-x[1])
    
        

    #print(len(equip_list))
    for i in range(len(equip_list)):
        NOW_userID_list[i]['equipInfo'] = equip_list[i]['equipInfo']

   
   
   #now = int(datetime.today().strftime('%Y%m%d'))
    

    context = {'Users' : Users, 'NOW_userID_list' : NOW_userID_list, 'goods' : goods}

    
    return render(request, 'user_main.html', context)
