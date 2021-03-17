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
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.id
#The user have one or more specified roles. For example a student can be a checker and have access to exam papers.
class UserManager(AbstractUser):
    role = models.ManyToManyField(Role)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(100)])
    def __str__(self):
        return self.name


SEX=(
('Male', 'Male'),
('Female', 'Female'),
)

DEPT=(
('College of Computer and Communication', 'College of Computer and Communication'),
('School of Electrical and Automation', 'School of Electrical and Automation'),
('Foreign Language Institute', 'Foreign Language Institute'),
('College of Science', 'College of Science'),
)
# TODO 3: Create a Student model

class Student(models.Model):
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=20,blank=False,null=False)
    last_name = models.CharField(max_length=20,blank=False,null=False)
    profile_picture = models.ImageField(upload_to='media/',blank=False)
    # user = models.OneToOneField(UserManager, on_delete=models.CASCADE, primary_key=True)
    enrolled = models.ManyToManyField(Subject, related_name='enrolled_subjects')
    approved = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'


# TODO 4: Create a Instructor model 

class Teacher(models.Model):
    id = models.CharField ("Teacher ID", max_length = 20, primary_key = True)
    name = models.CharField ('Name', max_length = 20)
    sex = models.CharField ('Gender', max_length = 6, choices = SEX, default = 'Male')
    Dept = models.CharField ('College', max_length = 40, choices = DEPT, default = None)
    email = models.EmailField ('mailbox', default = None)
    password = models.CharField ('password', max_length = 20, default = '000000')
    birth = models.DateField ('date of birth')

    class Meta:
        db_table='teacher'
        verbose_name = 'Teacher'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name;


class Question(models.Model):

    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    LEVEL={
        ('1','easy'),
        ('2','general'),
        ('3','difficult'),
    }
    id = models.AutoField(primary_key=True)
    subject = models.CharField ('Subject', max_length = 20)
    title = models.TextField (' ')
    optionA = models.CharField ('Aoption', max_length = 30)
    optionB = models.CharField ('Boption', max_length = 30)
    optionC = models.CharField ('Coption', max_length = 30)
    optionD = models.CharField ('Doption', max_length = 30)
    answer = models.CharField ('answer', max_length = 10, choices = ANSWER)
    level = models.CharField ('level', max_length = 10, choices = LEVEL)
    score = models.IntegerField ('score', default = 1)
    
    class Meta:
        db_table='question'
        verbose_name = 'Single choice question bank'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title);

class Paper(models.Model):
    pid = models.ManyToManyField (Question) #many to many
    Tid = models.ForeignKey (Teacher, on_delete = models.CASCADE) #Add foreign key
    subject = models.CharField ('Subject', max_length = 20, default = '')
    Major = models.CharField ('Applicable for test papers', max_length = 20)
    examtime=models.DateTimeField()
    
    def __str__(self):
        return self.Major;


class Grade(models.Model):
    sid = models.ForeignKey (Student, on_delete = models.CASCADE, default = '') # Add foreign key
    subject = models.CharField ('Subject',max_length = 20, default = '')
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.sid,self.grade);
