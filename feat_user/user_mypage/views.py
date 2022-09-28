from sign.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


def user_mypage(request):

    Users = User.objects.filter(studentID="20190811")
   

    context = {'Users' : Users}
    
    
    return render(request, 'user_mypage.html', context)
