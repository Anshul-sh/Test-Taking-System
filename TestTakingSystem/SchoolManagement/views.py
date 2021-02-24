from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from SchoolManagement.forms import RegisterForm

# Create your views here.

# TODO 1: Create the base templeate

# Home page for the complete Website 
def home(request):
    return render(request,'main\\base.html',{})
# TODO 2: Code for login
def profile(request, *args):
    return HttpResponse('<p>This is the login page test.{user.name}</p>')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None: 
                profile(request, user)
                return redirect('home')
            else: 
                return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
        else: 
            return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = RegisterForm()

    return render(request, 'register.html', {'form': form})