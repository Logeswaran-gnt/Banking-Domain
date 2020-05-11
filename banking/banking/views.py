from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

def login_page(request):
    print("==============================")
    print(request.user, request.user.is_authenticated)
    print(dir(request.session))
    print("==========================")
    if request.user.is_authenticated:
        return redirect('/home',{'name':'logesh'})
    else:
        return render(request, 'personalbanking/login.html')

def login_user(request):
    username = request.POST['Username']
    password = request.POST['Password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print(user)
        # history(request)
        return redirect('/home')
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # return redirect('/')

@login_required
def home_user(request):
    return render(request,'personalbanking/homepage.html',{'name':request.user})

def logout_user(request):
    logout(request)
    return redirect('/')