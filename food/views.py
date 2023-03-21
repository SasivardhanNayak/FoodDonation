from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User

# Create your views here.
def op(request):
    return render(request,'food/index.html')
def login(request):
    if request.method=='post':
        uname=request.post.get('username')
        email=request.post.get('email')
        pass1=request.post.get('password')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('signin')
    return render(request,'food/loginindex.html')
def signin(request):
    return render(request,'food/signin.html')
