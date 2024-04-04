from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.


User = get_user_model()
# Create your views here.
def index(request):
    members = User.objects.all()
    context = {
        'members': members
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('stores:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('stores:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('stores:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stores:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

