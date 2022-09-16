from .models import Renting, User, EquipCode, Equip
from django.shortcuts import render, redirect
from .import views
#





#신청서 작성
def rental(request):
    if(request.method == "GET"):

        Users = User.objects.filter(studentID="20190811")  

        equipid = request.GET.get('equipid')
        pr_equipids = Equip.objects.filter(equipID = equipid)

        context = {'Users' : Users, 'pr_equipids': pr_equipids}


        return render(request, 'user_rental.html', context)

    elif(request.method == "POST"):
        post = Renting()
        #post.userID = Users.values('studentID')
        #post.userName = Users.values('name')
        #post.userPhoneNum = Users.values('phoneNum')
        #post.equipID = equipid
        post.rentingDate = request.POST['rentdate']
        post.returningDate = request.POST['returndate']
        post.save()



    return redirect('../equipinfo', {'alert':'정상적으로 신청이 접수되었습니다'})



