from django.shortcuts import render
from faculty.models import Complain, Faculty
from django.contrib import messages
# Create your views here.
def new_complain(request):
    if request.method == 'POST':
        # create complain object and save it in the database
        complain_heading = request.POST.get('complain_name')
        complain_description = request.POST.get('complain_description')
        complain_registered = request.POST.get('complain_registered')
        registered_to = Faculty.objects.filter(faculty_id = complain_registered).first()
        complain_object = Complain(heading = complain_heading,description = complain_description, registered_to = registered_to)
        complain_object.save()
        messages.success(request, messages.SUCCESS, 'Your Complain has been registered successfully.')
        render('complain.html')
    else:
        print("GHAPLA HO RHA HAI")

