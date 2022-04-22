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
    return render(request,"index.html")


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
        if pass2 == pass1:
             myuser.save()
             port = 587  # For starttls
             smtp_server = "smtp.gmail.com"
             sender_email = "mycart2403@gmail.com"
             receiver_email = myuser.email
             password = 'Z3cs48gBO3hW'
             message= f"""\
    Subject: MY AWESOME CART
    Delivery Information
    Name :- {username}
    Email :- {email}
    address :- {password}
    Thankyou for creating account in Praaki's shopping site. Wish you a good day ahead!
    """
             context = ssl.create_default_context()
             with smtplib.SMTP(smtp_server, port) as server:
                try:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                except Exception as e:
                    print(e)

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
        loginemail = request.POST['loginemail']
        user = authenticate(username = loginusername, password = loginpassword,email = loginemail)

        if user is not None:
            login(request, user)
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "mycart2403@gmail.com"
            receiver_email = user.email
            password = 'Z3cs48gBO3hW'
            message = f"""\
              Subject: MY AWESOME CART
              Delivery Information
              Name :- {loginusername}
              Password :- {loginpassword}
              Someone try to login in your account. If you are not this then please change your password!
              """
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                try:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                except Exception as e:
                    print(e)


        else:
            messages.error(request, "Invalid, Try Again")
            return redirect("/")

    return HttpResponse("/")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
