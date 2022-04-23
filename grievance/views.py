import smtplib
from http import server
from profile import Profile
from sqlite3 import connect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# from validate_email import validate_email
import smtplib
import ssl


class Homepage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def form(request):
    return render(request, "form.html")

from random import random

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

    return HttpResponse("login")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully loged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid, Try Again")
            return redirect("/")

    return HttpResponse("handlelogin")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

