from django.shortcuts import render, redirect
from .form import SignUpForm, LoginForm, ChangeUsernameForm, ChangeEmailForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm


def index(request):
    return render(request, 'user/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            msg = 'user created'
            return redirect('core:home')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'user/register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'user/login.html', {'form': form, 'msg': msg})

@login_required
def profile(request):
    if request.method == 'POST':
        
        username_form = ChangeUsernameForm(request.POST, instance=request.user)
        email_form = ChangeEmailForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)


        if username_form.is_valid():
            username_form.save()

        if email_form.is_valid():
            email_form.save()

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)

        
        return redirect('user:profile')
    else:
        username_form = ChangeUsernameForm(instance=request.user)
        email_form = ChangeEmailForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'user/profile.html', {
        'username_form': username_form,
        'email_form': email_form,
        'password_form': password_form
    })