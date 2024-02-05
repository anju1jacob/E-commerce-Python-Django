from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            user=User.objects.create_user(username=username, email=email, password=password)
            customer=Customer.objects.create(user=user, address=address, phone=phone)
            messages.success(request,'Registration successfull..')
        except Exception as e:
            messages.warning(request,'invalid data input..')

    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)

        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'invalid login creditional..')

    return render(request,'account.html', context)

def sign_out(request):
    logout(request)
    return redirect('index')

