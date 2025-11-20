from django import forms
from .models import Student, StudentFeedback



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

class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = [
            'name', 'email', 'age', 'satisfaction', 'gender',
            'enrolled', 'join_date', 'course', 'comments'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'age': forms.NumberInput(attrs={'min': 10, 'max': 100}),
            'satisfaction': forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 10}),
            'gender': forms.RadioSelect(),
            'enrolled': forms.CheckboxInput(),
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'course': forms.TextInput(attrs={'placeholder': 'Your course name'}),
            'comments': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Any feedback…'}),
        }