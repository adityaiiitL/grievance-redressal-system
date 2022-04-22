from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import HttpResponse
from faculty.models import Faculty, Complain
from student.models import Student
# Create your views here.
def reports(request): 
    return render(request, 'faculty/index.html')

# API's here
def search(request):
    if request.method != 'POST':
        return HttpResponse("<h1> HTTP Method Not Allowed </h1>")
    else: 
        query = request.POST.get('query', None)
        complains = Complain.objects.filter(Q(heading=query)|Q(description=query))
        return render(request, 'faculty/search.html', {"complains":complains})
    