from django.forms import ModelForm ,Form
from django.contrib.auth.forms import UserCreationForm
from SchoolManagement.models import Student, UserManager
from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import RadioSelect, Textarea
from django.forms import ModelForm
from .models import Quiz , Course , Subject, MCQuestion , Answer
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = UserManager
        fields = ['email','username','first_name','last_name','password']

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'gender', 'course_id', 'session_year_id', 'birth','profile_pic']


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserManager
        fields = ('username', 'password')

class QuestionForm(Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)

class EssayForm(Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))

class Createexam(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class MCquestionForm(ModelForm):
    class Meta:
        model = MCQuestion 
        fields = '__all__'

class MCanswerForm(ModelForm):
    class Meta:
        model = Answer 
        fields = '__all__'
