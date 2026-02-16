from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()


def register(request):
    print(User.objects.all())
    """Реєстрація нового користувача"""
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматичний логін після реєстрації
            messages.success(request, "Реєстрація успішна! Ви увійшли в систему.")
            return redirect("portfolio:index")  # змінити на потрібний route
    return render(request, "account/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("portfolio:index")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("portfolio:index")
        else:
            messages.error(request, "Неправильний логін або пароль")

    return render(request, "account/login.html")

@login_required
def profile(request):
    user = request.user
    return render(request, "account/profile.html", {"user": user})
