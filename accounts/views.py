from django.shortcuts import render,redirect   
from django.http import HttpResponse
from django.contrib.auth.models import User,auth  # for ORM (import models for user)
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username= username, password = password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,'Invalid credentials')   
            return redirect('login')
       
    else :    
        # return render(request, 'register.html',{'msg':'No message'})   (1)
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # create new user object
        if password1 ==password2:
            if User.objects.filter(username= username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
                # return render(request, 'register.html',{'msg' : 'Username Taken'})   (1)
            elif User.objects.filter(email= email).exists():
                messages.info(request,'email Taken')
                return redirect('register')  
                # return render(request, 'register.html',{'msg' : 'Email Taken'})       (1)
            else:           
                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, password = password1, email = email)
                user.save()
                print('USER CREATED ! WELCOME ABOARD {}'.format(username) )
                return redirect('login')    # import redirect
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
            # return render(request, 'register.html',{'msg' : 'Password does not match'})    (1)
    else :    
        # return render(request, 'register.html',{'msg':'No message'})   (1)
        return render(request, 'register.html')

   # (1) uncomment the code to send msg back in different way.     

