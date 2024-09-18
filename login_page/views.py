from django.shortcuts import redirect, render 

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from login_page import settings
# from django.core.mail import send_mail
import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import translators as ts





# Create your views here.
def home(request):
    return render(request, "index.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            # return redirect('home', {"fname":fname})
            messages.success(request ,f"Namaste, {user.username} 🔓 You are successfully logged in! 🎉") 
            return redirect('home')

        else:
            messages.error(request, "Invalid Username or password please try again!")
            return redirect('signin')
    return render(request, "signin.html")



def signout(request):
    logout(request,)
    messages.success(request, f"Goodbye, 🔒 You are successfully logged out! 👋")
    return redirect('home')


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try another username.")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered try with other email.")
            return redirect('signup')

        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        if pass1 != pass2:
            messages.error(request, "Password did not match Re-enter password")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric.")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account created successfully.")

        # Welcome Message for email

        # subject = "Welcome to login-page- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Login!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nGaurav Mathur"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        return redirect('signin')

    
    return render(request,'signup.html')

# -----------------------------------------------------------------------------------------------------------------------

