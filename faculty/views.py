from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import HttpResponse
from .models import Faculty, Complain
from .forms import ComplainForm


# Create your views here.
def report(request):
    allcomplains = Complain.objects.all()
    allfaculty = Faculty.objects.all()
    return render(request, 'faculty/index.html', {'allcomplains': allcomplains, 'allfaculty': allfaculty})


# API's here
def search(request):
    if request.method != 'POST':
        return HttpResponse("<h1> HTTP Method Not Allowed </h1>")
    else:
        query = request.POST.get('query', None)
        complains = Complain.objects.filter(Q(heading=query) | Q(description=query))
        return render(request, 'faculty/search.html', {"complains": complains})


def index(request):
    pass


# def index(request):

def read(request, id):
    vi = Complain.objects.filter(complain_id=id)[0]

    context = {'vi': vi}
    return render(request, "faculty/view.html", context)
#
#
# def Complain_(request):
#     complains = Complain.objects.all()
#     return render(request, "complain.html", context={'complains': complains})


def complainform(request):
    if request.method == "POST":
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComplainForm()
    return render(request, 'complainform.html', {'form': form})
