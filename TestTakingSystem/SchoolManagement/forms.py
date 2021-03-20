from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from SchoolManagement.models import Student, UserManager

class UserForm(ModelForm):
    class Meta:
        model = UserManager
        fields = ['email','username','first_name','last_name','password']

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'gender', 'course_id', 'session_year_id', 'birth','profile_pic']


