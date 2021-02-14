from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# TODO 1: Create the base templeate

# Home page for the complete Website 
def home(request):
    return render(request,'main\\base.html',{})
# TODO 2: Code for login
def login(request, *args):
    return HttpResponse('<p>This is the login page test.</p>')
