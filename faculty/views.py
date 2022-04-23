from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import Faculty, Complain
from student.models import Student


# Create your views here.
today_date = date.today() 
def update_tree():
    datetime.datetime()
    if(date.today() != today_date):
        today_date = date.today()
        update_obj = Complain.objects.filter(complain_response_date__date= today_date) 
        for obj in update_obj:
            obj.complain_response_date = today_date+timedelta(days=2)
            # Request elevated to the parent node
            obj.registered_to = obj.registered_to.parent


def reports(request):
    #meri logic 
    update_tree()
    return render(request, 'faculty/index.html')


# API's here
def search(request):
    if request.method != 'POST':
        return HttpResponse("<h1> HTTP Method Not Allowed </h1>")
    else:
        query = request.POST.get('query', None)
        complains = Complain.objects.filter(Q(heading=query)|Q(description=query))
        return render(request, 'faculty/search.html', {"complains":complains})

def index(request):
    pass
