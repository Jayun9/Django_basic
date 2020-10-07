from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User1

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data = {}
        if not(username and password and re_password and useremail):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user1 = User1(
                username = username,
                password = make_password(password),
                useremail = useremail
            )
            user1.save()
        return render(request, 'register.html',res_data)