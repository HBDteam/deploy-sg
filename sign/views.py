from .models import User, Manager
from django.shortcuts import render, redirect

'''
    sign.html에서 onclick 시 ajax 통신으로 post/get을 구현 할 예정임.
'''


# load sign page
def sign(request):
    # /sign GET 요청이 오면 sign.html 페이지를 로드한다.
    return render(request, 'sign.html')

# sign up
def signup(request):
    if request.method == 'POST':
        # 비밀번호가 동일한 지 검사한다.
        if request.POST['pass'] == request.POST['confirm']:
            # 동일하다면 User 테이블에 사용자를 추가한다.
            user = User(studentID=request.POST['user'], password=request.POST['pass'], name=request.POST['name'], email=request.POST['email'], phoneNum=request.POST['phone'], isEnrolled=request.POST['isEnrolled'])
            user.save()
        else:
            # error
            return 0
    return render(render, 'sign.html')

# sign in
def signin(request):
    if request.method == 'POST':
        userid = request.POST['user']
        userpass = request.POST['pass']
        # 테이블에서 해당 아이디와 비밀번호에 해당되는 행을 가져온다.
        queryset = User.objects.filter(studentID=userid, password=userpass)
        # 존재하면 다음 페이지로 redirect
        if queryset.exists() == True:
            return redirect('/user_main')
        # 존재하지 않으면 에러 메시지를 전달하고, 첫 화면으로 돌아간다.
        else:
            return render(request, 'sign.html', {'error':'아이디와 비밀번호가 일치하지 않습니다.'})
    return render(render, 'sign.html')