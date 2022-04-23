from django.contrib.auth.models import Permission, User
from django.shortcuts import render
from pip import main
from faculty.models import Complain, Faculty
from django.contrib import messages
# Create your views here.
def new_complain(request):
    if request.method == 'POST':
        # create complain object and save it in the database
        complain_heading = request.POST.get('complain_name')
        complain_description = request.POST.get('complain_description')
        complain_registered = request.POST.get('complain_registered')
        complain_response_date = request.POST.get('complain_response_date')
        registered_to = Faculty.objects.filter(faculty_id = complain_registered).first()
        complain_object = Complain(heading = complain_heading,description = complain_description, registered_to = registered_to,
        complain_response_date = complain_response_date)
        complain_status = request.POST.get('complain_status')
        complain_object.save()
        messages.success(request, 'Your Complain has been registered successfully.')
        return render('complain.html')
    else:
        print("GHAPLA HO RHA HAI")

def index(request):
    if request.user.is_authenticated():
        User.objects.get()

if __name__ == "__main__":
    print("ghapla hota rahega"); 