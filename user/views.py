from django.shortcuts import render, redirect
from .form import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'user/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('user:login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'user/register.html', {'form': form, 'msg': msg})

def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('core:home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'user/login.html', {'form': form, 'msg': msg})