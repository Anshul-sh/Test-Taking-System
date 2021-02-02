from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# TODO 1: Create the base templeate

# Home page for the complete Website 
def home(request):
    return render('<p>This is the home page test.</p>')
# TODO 2: Code for login
def login(request, *args):
    return HttpResponse('<p>This is the login page test.</p>')
