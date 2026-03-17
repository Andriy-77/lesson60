from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "email", "content"]
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше імʼя"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Ваш коментар"}
            ),
        }
