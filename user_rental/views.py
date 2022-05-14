from .models import Renting
from django.shortcuts import render, redirect
from .import views
#





#신청서 작성
def rental(request):
    if(request.method == "GET"):
        return render(request, 'user_rental.html' )

    elif(request.method == "POST"):
        post = Renting()
        #post.userID = request.POST['userid']
        #post.userName = request.POST['username']
        #post.userPhoneNum = request.POST['phonenum']
        #post.equipID = request.POST['equipid']
        post.rentingDate = request.POST['rentdate']
        post.returningDate = request.POST['returndate']
        post.serialnum = request.POST['senum']
        post.save()
    return redirect('../equipinfo', {'alert':'정상적으로 신청이 접수되었습니다'})

