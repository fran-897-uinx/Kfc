from django import forms
from .models import Student, Reservation, Menu

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "phone_number", "reason"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter your full name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter your email address",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter your phone number",
                }
            ),
            "reason": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                    "rows": 4,
                    "placeholder": "Why do you want to register?",
                }
            ),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["email", "phone_number"]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter your registered email address",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter your registered phone number",
                }
            ),
        }


class ReservationForm(forms.ModelForm):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # or use SelectMultiple
        required=False,
        label="Select Menu Items",
    )

    class Meta:
        model = Reservation
        fields = ["name", "email", "guest_phone_num", "date", "meassage", "menu_items"]
        date = forms.DateTimeField(
            widget=forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "input input-bordered w-full",
                },
                format="%Y-%m-%dT%H:%M",
            )
        )
