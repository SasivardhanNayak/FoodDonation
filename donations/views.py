from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'food/index.html')

def dashboard(request):
    foods=food.objects.all()
    cloth=cloths.objects.all()
    return render(request,"food/dashboard.html",{"foods":foods,"cloths":cloth})

def Request(request):
    if request.method=="POST":
        user=request.user
        Address=request.POST.get("address")
        contact=request.POST.get("mobile")
        item_id=request.POST.get("item_id")


def Login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Login successfull!')
            return HttpResponseRedirect(reverse('index'))
        else:
            print("fail")
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return render(request,"food/login.html")
    return render(request,'food/login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get("email")
        password = request.POST.get('password')

        # Check if the username is available
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, 'This mobile number is already exits! Try loging in.')
            return render(request, 'food/signup.html')

        # Create the new user object
        user = User.objects.create_user(username=username, email=email,password=password)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Account created! Please login')
        return HttpResponseRedirect(reverse('login'))
    
    return render(request, 'food/signup.html')
    


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out!')
    return render(request,"users/login.html")


def donate_food(request):
    if request.method=="POST":
        user=request.user
        name=request.POST.get("foodname")
        image=request.POST.get("foodimage")
        food_type=request.POST.get("meal")
        food_category=request.POST.get("image-choice")
        qnt=request.POST.get("quantity")
        food_item=food(user=user,name=name,image=image,food_type=food_type,category=food_category,qnt=qnt)
        food_item.save()
        return render(request,"food/donatefood.html")
    return render(request,"food/donatefood.html")


def donate_cloth(request):
    if request.method=="POST":
        user=request.user
        name=request.POST.get("clothname")
        image=request.POST.get("clothimage")
        cloth_type=request.POST.get("cloth_type")
        cloth_category=request.POST.get("cloth-choice")
        qnt=request.POST.get("quantity")
        cloth_item=cloths(user=user,name=name,image=image,cloth_type=cloth_type,category=cloth_category,qnt=qnt)
        cloth_item.save()
        return render(request,"food/donatecloth.html")
    return render(request,"food/donatecloth.html")


def placerequest(request):
    if request.method=="GET":
        request_type=request.GET["request_type"]
        if request_type=="food":
            item_id=request.GET["food_id"]
            item=food.objects.get(food_id=item_id)
        if request_type=="cloth":
            item_id=request.GET["food_id"]
            item=cloths.objects.get(cloths_id=item_id)
        return render(request,"food/placerequest.html",{"item":item,"request_type":request_type,"item_id":item_id})
    if request.method=="POST":
        item_id=request.POST.get("item_id")
        address=request.POST.get("address")
        mobile=request.POST.get("mobile")
        user=request.user
        request_type=request.POST.get("request_type")
        if request_type=="food":
            item=food.objects.get(food_id=item_id)
            item.status=False
            item.save()
        if request_type=="cloth":
            item=cloths.objects.get(cloth_id=item_id)
            item.status=False
            item.save()
        new_request=Donation_Request(request_type=request_type,item_id=item_id,user=user,Address=address,contact=mobile)
        new_request.save()
        return HttpResponseRedirect(reverse("dashboard"))
    return HttpResponseRedirect(reverse("dashboard"))
        
def profile(request):
    user=request.user
    food_donations=food.objects.filter(user=user)
    cloth_donations=cloths.objects.filter(user=user)
    return render(request,"food/profile.html",{"food_donations":food_donations,"cloth_donations":cloth_donations})