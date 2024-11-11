from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'grade', 'major']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter major'}),
        }
