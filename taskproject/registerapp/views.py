from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login (request):
    if request.method =='POST':
        v1=request.POST['username']
        v5=request.POST['password']
        j3=auth.authenticate(username=v1,password=v5)
        if j3 is not None:
            auth.login(request,j3)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')


    return render(request, "login.html")
def register (request):
    if request.method =='POST':
        v1 = request.POST['username']
        v2 = request.POST['first_name']
        v3 = request.POST['last_name']
        v4 = request.POST['email']
        v5 = request.POST['password']
        v6 = request.POST['password1']

        if v5==v6:
            if User.objects.filter(username=v1).exists():
                messages.info(request,"username already exit")
                return redirect('register')
            elif User.objects.filter(email=v4).exists():
                messages.info(request,"email already exit")
                return redirect('register')
            else:
                v7=User.objects.create_user(username=v1,first_name=v2,last_name=v3,email=v4,password=v5)

                v7.save();
                return redirect ('login')

        else:
            messages.info(request,"incorrect password")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def logout (request):
    auth.logout(request)
    return redirect('/')