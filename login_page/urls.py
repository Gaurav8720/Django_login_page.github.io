from django.contrib import admin
from django.urls import path, include
from login_page import views as log

urlpatterns = [
    path("", log.home, name="home"),
    path("signin/", log.signin, name="signin"),
    path("signout/", log.signout, name="signout"),
    path("signup/", log.signup, name="signup"),
   
    
]