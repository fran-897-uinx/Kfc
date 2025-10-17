from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'phone_number', 'reason']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Enter your full name',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Enter your age',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Enter your email address',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'input input-bordered w-full',
                'placeholder': 'Enter your phone number',
            }),
            'reason': forms.Textarea(attrs={
                'class': 'textarea textarea-bordered w-full',
                'rows': 4,
                'placeholder': 'Why do you want to register?',
            }),
        }
