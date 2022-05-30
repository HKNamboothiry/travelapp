from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place, TeamMembers

# Create your views here.
def helloWorld(request):
    obj=Place.objects.all()
    team_memb = TeamMembers.objects.all()
    return render(request, "index.html",{'result':obj, 'teamMembers':team_memb})

#this is the register function
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        confirm_password = request.POST['confirmpassword']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('Register')
            else:
                user=User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save();
                print('user created successfully')
                return redirect('login')
        else:
            messages.info(request, "Passwords Missmatch")
    return render(request, "register.html")

#this is the login function of the application
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, "login.html")

#this is the logout function of the application
def logout(request):
    auth.logout(request)
    return redirect('/')