from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Manager
from django.shortcuts import render, redirect
from django.contrib.auth.models import User as UUser# 추가

from argon2 import PasswordHasher
from django.contrib import auth # 추가

'''
    sign.html에서 onclick 시 ajax 통신으로 post/get을 구현 할 예정임.
'''
# sign up
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                        studentID=request.POST['username'],
                        password=PasswordHasher().hash(request.POST['password1']).encode('utf-8'),
                        name=request.POST['name'],
                        email=request.POST['email'],
                        phoneNum=request.POST['phone'],
                        isEnrolled=request.POST['isEnrolled'])
            user.save()
            return render(request, 'sign.html')
    return render(request, 'sign.html')

# sign in
def signin(request):
    if request.method == 'GET':
        return render(request, 'sign.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None) # 사용자가 입력한 id 가져오기
        password = request.POST.get('password',None) # 사용자가 입력한 pwd 가져오기 
        res_data = {} # front로 보낼 데이터
        if not (username and password):
            res_data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'sign.html')
        else:
            # 사용자, 관리자 체크하기
            if User.objects.filter(studentID=username).exists() == True: # 사용자
                login_user = User.objects.get(studentID=username)
                if PasswordHasher().verify(login_user.password.decode('utf-8'),password):
                    user_id = login_user.studentID
                    password = login_user.password
                    request.session['user'] = user_id
                    if UUser.objects.filter(username=user_id).exists() == True:
                        user = UUser.objects.get(username=user_id)
                        auth.login(request, user)
                        return redirect('/feat_user/user_main/') # 사용자 페이지로 이동
                    else:
                        user = UUser.objects.create_user(user_id,login_user.password.decode('utf-8'))
                        auth.login(request, user)
                        return redirect('/feat_user/user_main/') # 사용자 페이지로 이동
                else:
                    print('실패')
            elif Manager.objects.filter(mID= username).exists() == True:
                manager_user =  Manager.objects.get(mID= username)
                if PasswordHasher().verify(manager_user.mPassword.decode('utf-8'),password):
                    user_id = manager_user.mID
                    request.session['user'] = user_id
                    return redirect('/admin_main') # 사용자 페이지로 이동
    else: return redirect('sign.html')
