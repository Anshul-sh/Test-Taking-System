from django import forms
from django.contrib.auth.forms import UserCreationForm
from SchoolManagement.models import Student

class RegisterForm(UserCreationForm):
 def __init__(self, *args, **kwargs):
  super(RegisterForm, self).__init__(*args, **kwargs)
  # do not require password confirmation
  del self.fields['password2']

 class Meta:
  model = Student
  fields = ['email', 'first_name', 'last_name','profile_picture']
  
  labels = {
    'email': 'email',
   'first_name': 'First Name',
   'last_name': 'Last Name',
   'profile_picture': 'profile picture'
  }
  
