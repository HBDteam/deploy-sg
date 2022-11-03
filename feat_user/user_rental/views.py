from .models import Renting, User, EquipCode, Equip
from django.shortcuts import render, redirect
from .import views



#신청서 작성
def rental(request):
    login_user_ID = request.user.username
    Users = User.objects.filter(studentID=login_user_ID)
    post = Renting()
    post.userPhoneNum = Users.values('phoneNum')
    post.userName = Users.values('name')
    post.userID_no = Users.values('studentID')
    

    if(request.method == "GET"):
        
        equipid = request.GET.get('equipid')
        pr_equipids = Equip.objects.filter(equipID = equipid) 
        context = {'Users' : Users, 'pr_equipids': pr_equipids }
        return render(request, 'user_rental.html', context)

    if(request.method == "POST"):     
        #post.userID = request.POST['userid']  
        post.rentingDate = request.POST['rentdate']
        post.returningDate = request.POST['returndate']
        post.equipID_no = request.POST.get("equipids", "")
        #post.returningDate = request.POST['equipid']
        #print(a)
        #post.userID = request.POST['studentID']
        
        
        post.save()   

        return redirect('../equipinfo', {'alert':'정상적으로 신청이 접수되었습니다'})
