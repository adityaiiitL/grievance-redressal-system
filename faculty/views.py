from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import Faculty, Complain
from student.models import Student
from faculty.forms import ComplainForm


# Create your views here.
def report(request):
    allcomplains = Complain.objects.all()
    allfaculty = Faculty.objects.all()
    return render(request, 'faculty/index.html', {'allcomplains': allcomplains, 'allfaculty':allfaculty})
today_date = date.today() 
# def update_tree():
#     datetime.datetime()
#     if(date.today() != today_date):
#         today_date = date.today()
#         update_obj = Complain.objects.filter(complain_response_date__date= today_date) 
#         for obj in update_obj:
#             obj.complain_response_date = today_date+timedelta(days=2)
#             # Request elevated to the parent node
#             obj.registered_to = obj.registered_to.parent


def reports(request):
    #meri logic 
    # update_tree()
    complains = Complain.objects.all()[0:10]
    return render(request, 'faculty/index.html', {"complains":complains})
today_date = None

def update_tree():
    global today_date
    if(today_date is None or today_date.day < datetime.now().day):
        today_date = datetime.now()
        update_obj = Complain.objects.filter(complain_response_date__day < today_date.day)
        for obj in update_obj:
            obj.complain_response_date = today_date+timedelta(days=2)
            # Request elevated to the parent node
            obj.registered_to = obj.registered_to.parent

# today_date = None

# def update_tree():
#     global today_date
#     if(today_date is None or today_date < datetime.now()):
#         today_date = datetime.now()
#         update_obj = Complain.objects.filter(complain_response_date__minute < today_date.minute)
#         for obj in update_obj:
#             obj.complain_response_date = today_date+timedelta(minutes=2)
#             # Request elevated to the parent node
#             obj.registered_to = obj.registered_to.parent


def report(request):
    update_tree()
    allcomplains = Complain.objects.all()
    allfaculty = Faculty.objects.all()
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

# def index(request):

def read(request, id):
    vi = Complain.objects.filter(complain_id=id )[0]

    context = {'vi':vi}
    return render(request, "faculty/view.html", context)

def Complain_(request):
    allcomplains = Complain.objects.all()
    return render(request, "complain.html", context={'allcomplains': allcomplains})


def complainform(request):
    if request.method == "POST":
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComplainForm()
    return render(request, 'complainform.html', {'form': form})

