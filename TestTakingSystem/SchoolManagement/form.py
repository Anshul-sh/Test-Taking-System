from django import forms
from SchoolManagement.models import Student
from django.db import models
 
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
class FaceidFrom(forms.Form):
    image_field =  models.ImageField(uploadto='images')


