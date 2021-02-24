from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

# TODO 1: Connect django with mongoDB

# The role is the entity that decides which permissions are to be given to the user.
class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  STUDENT = 1
  TEACHER = 2
  SECRETARY = 3
  SUPERVISOR = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (SECRETARY, 'secretary'),
      (SUPERVISOR, 'supervisor'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()
#The user have one or more specified roles. For example a student can be a checker and have access to exam papers.
class UserManager(AbstractUser):
    role = models.ManyToManyField(Role)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(100)])
    def __str__(self):
        return self.name
# TODO 3: Create a Student model

class Student(models.Model):
    user = models.OneToOneField(UserManager, on_delete=models.CASCADE, primary_key=True)
    enrolled = models.ManyToManyField(Subject, related_name='enrolled_subjects')
    approved = models.BooleanField(default=False)


# TODO 4: Create a Instructor model 

class Teacher(models.Model):
    user = models.OneToOneField(UserManager, on_delete=models.CASCADE, primary_key=True)
    assigned = models.ManyToManyField(Subject, related_name='assigned_subjects')
    approved = models.BooleanField(default=False)

class ImageTest(models.Model):
    image = models.ImageField(upload_to='images/', help_text='test image')