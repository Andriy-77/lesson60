from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    if user != request.user:
        raise HttpResponseForbidden("Ви не маєте доступу до цього профілю.")     # type: ignore

    if request.method == 'POST':
        new_email = request.POST.get('email')
        user.email = new_email
        user.save()
        
        context = {
            'user': user
        }
    return render(request, 'profile.html', context)
