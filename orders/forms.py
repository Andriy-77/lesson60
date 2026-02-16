from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "project_description", "budget", "deadline"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше ім'я"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Ваш email"}
            ),
            "project_description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Опишіть ваш проект"}
            ),
            "budget": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Бюджет (USD)"}
            ),
            "deadline": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Терміни реалізації",
                    "required": False,
                }
            ),
        }
        labels = {
            "name": "Ім'я",
            "email": "Email",
            "project_description": "Опис проекту",
            "budget": "Бюджет (USD)",
            "deadline": "Терміни реалізації",
        }
