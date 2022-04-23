from django import forms
<<<<<<< HEAD
from .models import Complain
=======
from faculty.models import Complain
>>>>>>> bef1943ef1d78e3eafc11a41d738ab6bb20e117c


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = "__all__"
