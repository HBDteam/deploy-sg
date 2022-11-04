from .models import Renting, User, EquipCode, Equip
from django.shortcuts import render, redirect
from .import views



#신청서 작성
def rental(request):
    token_userID= request.user.username
    rent_Users = User.objects.filter(studentID=token_userID)
    rentpost = Renting()
    rentpost.userPhoneNum = rent_Users.values('phoneNum')
    rentpost.userName = rent_Users.values('name')
    rentpost.userID_no = rent_Users.values('studentID')
    

    if(request.method == "GET"):

        equipid = request.GET.get('equipid')
        pr_equipids = Equip.objects.filter(equipID = equipid) 
        context = {'Users' : rent_Users, 'pr_equipids': pr_equipids }
        return render(request, 'user_rental.html', context)

    if(request.method == "POST"):     
        #post.userID = request.POST['userid']  
        rentpost.rentingDate = request.POST['rentdate']
        rentpost.returningDate = request.POST['returndate']
        rentpost.equipID_no = request.POST.get("equipids", "")
        #post.returningDate = request.POST['equipid']
        #print(a)
        #post.userID = request.POST['studentID']

        
        rentpost.userID = None
        rentpost.equipID = None
        
        rentpost.save()   

        return redirect('../user_equipment', {'alert':'정상적으로 신청이 접수되었습니다'})