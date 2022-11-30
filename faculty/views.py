from datetime import datetime, date, timedelta
from tkinter import N
from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import Faculty, Complain
from student.models import Student
from faculty.forms import ComplainForm
from django.contrib import messages

# Create your views here.

today_date = None
def update_tree():
    global today_date
    if(today_date is None or today_date.day < datetime.now().day):
        today_date = datetime.now()
        update_obj = Complain.objects.filter(complain_response_date.date() < today_date)
        for obj in update_obj:
            obj.complain_response_date = today_date+timedelta(days=2)
            obj.registered_to = obj.registered_to.parent
    


def report(request):
    update_tree()
    if(request.user.is_authenticated):
        allfaculty = Faculty.objects.filter(contact=request.user.email)
        lst = [item.contact for item in allfaculty]
        if(len(lst) == 0):
            messages.error(request, 'Only faculty is allowed to view complaints')
            return redirect('/home')
        if(lst[0] == request.user.email):
            allcomplains = Complain.objects.filter(registered_to__contact=request.user.email)
            return render(request, 'faculty/index.html', {'allcomplains': allcomplains, 'allfaculty':allfaculty})
        else:
            messages.error(request, 'Only faculty is allowed to view complaints')
            return redirect('/home')
    else:
        messages.error(request, 'Only faculty is allowed to view complaints')
        return redirect('/home')
    return render(request, 'faculty/index.html', {'allcomplains': allcomplains, 'allfaculty':allfaculty})

# API's here
def search(request):
    if request.method != 'POST':
        return HttpResponse("<h1> HTTP Method Not Allowed </h1>")
    else:
        query = request.POST.get('query', None)
        allcomplains = Complain.objects.filter(Q(heading=query) | Q(description=query))
        return render(request, 'faculty/search.html', {"allcomplains": allcomplains})


def index(request):
    pass

def read(request, complain_id):
    slug = 10
    vi = Complain.objects.filter(id=complain_id).first()
    return render(request, "faculty/view.html", {'vi':vi})

def Complain_(request):
    allcomplains = Complain.objects.all()
    return render(request, "complain.html", context={'allcomplains': allcomplains})

def elevateComplain(request, complain_id):
    update_tree()
    complain = Complain.objects.filter(id=complain_id).first()
    if(complain.registered_to.parent is not None):
        complain.registered_to = complain.registered_to.parent
        complain.complain_response_date = datetime.now() + timedelta(days=2)
        complain.save()
        messages.success(request, "Complain elevated successfully")
        return redirect('/faculty/report')
    else:
        messages.error(request, "Complain can't be elevated further")
        return redirect('/aculty/report')

def completeComplain(request, complain_id):
    complain = Complain.objects.filter(id=complain_id).first()
    complain.completed = True
    complain.save()
    messages.success(request, "Complain completed successfully")
    return redirect('/faculty/report')

def complainform(request):
    if request.method == "POST":
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Your complain has been successfully created")
            return redirect('/')
    else:
        if(request.user.is_authenticated):
            form = ComplainForm()
        else:
            messages.error(request, 'Log in to submit a complaint')
            return redirect('/')
    return render(request, 'complainform.html', {'form': form})

