from django import forms
from faculty.models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = "__all__"
