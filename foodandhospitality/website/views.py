from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage, send_mail
from website.models import uprofileform, uprofile

# import requests

# Create your views here.


def em():
    send_mail('form django after fixing issue', 'mana isp issue ', 'maremandasreekrishna@gmail.com',
              ['maremandasreekrishna@gmail.com', 'jurendrav@gmail.com'])


def home(request):
    return render(request, 'home.html')


def loginuser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['pass']
        user = auth.authenticate(request, username=uname, password=passw)
        print(user)
        if user is not None:
            print('authenticated')
            auth.login(request, user)
            return render(request, 'home.html')
    return render(request, 'login.html')


def logoutuser(request):
    auth.logout(request)
    return redirect('/')


def Register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pass']
        conpass = request.POST['conpass']
        email = request.POST['email']
        if password == conpass:
            user = User.objects.create_user(
                username=uname, password=password, email=email)
            user.save()
            # email = EmailMessage('confirmation mail', 'You have successfully registered in zwiggy we look farward to serve you',
            #                      to=[email])
            # email.send()
            return redirect('/')
        else:
            return render(request, 'Registration.html', {'errormsg': 'please fill the fields correctly'})

    else:
        return render(request, 'Registration.html')


def upload(request):
    if request.method == 'POST':
        form = uprofileform(request.POST, request.FILES,
                            )
        if form.is_valid():
            profile = form.save(commit=False)
            profile.meta = request.user
            profile.save()
            return HttpResponse('success')
    else:
        form = uprofileform()
    return render(request, 'upload.html', {'form': form})


def profile(request):
    # print(request.method, "    ", user.is_authenticated)
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = uprofileform()
            # print(request.user.u)
            try:
                p = uprofile.objects.get(meta=request.user.id)
            except:
                return render(request, "user_profile.html", {'form': form})
            return render(request, "user_profile.html", {'form': form, 'url': p.profileimg.url})
        return redirect('loginuser')
    else:
        a = request.user
        if a is not None:
            form = uprofileform(request.POST, request.FILES)
            # pr = uprofile.objects.get(meta=request.user.id)
            # if pr.profileimg:
            #     pr.profileimg = form.Meta.model.profileimg
            if form.is_valid():
                p = form.save(commit=False)
                p.meta = request.user
                p.save()
                return HttpResponse('successfully updated profile')
        return redirect('loginuser')


def restsview(request):
    return render(request, 'displayrest.html')


def contactus(request):
    return render(request, 'contactus.html')


def foodcard(request):
    return render(request, 'foodindex.html', {'d': [1, 2, 3, 4, 5, 6]})


def booktable(request):
    pass
