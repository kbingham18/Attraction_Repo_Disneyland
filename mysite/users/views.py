from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib import admin
import os


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

@login_required
def editprofile(request):
    # username = os.getlogin()
    # user = Profile.objects.get(user=username)
    user = request.user.profile
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'users/profile-form.html', {'form': form,  'item': request.user.profile})
