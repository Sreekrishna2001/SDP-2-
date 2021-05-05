from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(req):
    return render(req,'login.html')


def Register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname="None"
        uname=request.POST['uname']
        password=request.POST['pass']
        email=request.POST['email']
        user=User.objects.create_user(username=uname,password=password,email=email,first_name=fname,last_name=lname)
        user.save()
        return redirect('/')
    else:
        return render(request,'Registration.html')
