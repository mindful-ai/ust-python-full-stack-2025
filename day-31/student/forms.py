from django import forms
from .models import Student



class ContactAdminForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'course']

'''
ModelForm -> automatically creates a form from a model
Meta -> metadata -> inner class that is used to configure the form
     -> which models to use and while fields to include
'''