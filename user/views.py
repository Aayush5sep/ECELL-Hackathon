from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from .models import BuyerDetails,SellerDetails
import requests
# Create your views here.

def loginpage(request):
    return render(request,'user/login.html')

def sepage(request):
    return render(request,'user/sesignup.html')

def bypage(request):
    return render(request,'user/bysignup.html')

def userinfo(request):
    return render(request,'user/userinfo.html')

def loginn(request):
    # user.groups.filter(name="some-group").exists()
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return render(request,'homepage.html')
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

def signupse(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        age=request.POST['age']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']

        if age<18:
            return HttpResponse("You are not eligible as a seller !")
        newuser=User.objects.create_user(username,email,password)
        user=authenticate(username=username,password=password)
        login(request,user)
        g = Group.objects.get(name='Seller')
        g.user_set.add(user)
        userd=SellerDetails(user=user,fname=fname,lname=lname,phone=phone,age=age,city=city,state=state,country=country)
        userd.save()
        messages.success(request,"User Account Created Successfully")
        return render(request,'homepage.html')
    else:
        return HttpResponse("Creating new user account failed !")

def signupby(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']

        newuser=User.objects.create_user(username,email,password)
        user=authenticate(username=username,password=password)
        login(request,user)
        g = Group.objects.get(name='Buyer')
        g.user_set.add(user)
        userd=BuyerDetails(user=user,fname=fname,lname=lname,phone=phone)
        userd.save()
        messages.success(request,"User Account Created Successfully")
        return render(request,'homepage.html')
    else:
        return HttpResponse("Creating new user account failed !")

def logot(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return render(request,'homepage.html')