from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

# TODO 1: Connect django with mongoDB

class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    object=models.Manager()

class UserManager(AbstractUser):
    user_role_data = ((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_role = models.CharField(default=1,choices=user_role_data,max_length=10)

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()   

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    code = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(100)])
    staff_id=models.ForeignKey(UserManager,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
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
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(UserManager,on_delete=models.CASCADE)
    sex = models.CharField ('Gender', max_length = 6, choices = SEX, default = 'Male')
    birth = models.DateField ('date of birth')
    profile_pic=models.FileField()
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    enrolled_subject = models.ManyToManyField(Subject, related_name='enrolled_subjects')
    approved = models.BooleanField(default=False)
    objects = models.Manager()


# TODO 4: Create a Instructor model 

class Teacher(models.Model):
    id = models.CharField ("Teacher ID", max_length = 20, primary_key = True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    sex = models.CharField ('Gender', max_length = 6, choices = SEX, default = 'Male')
    Dept = models.CharField ('College', max_length = 40, choices = DEPT, default = None)
    birth = models.DateField ('date of birth')
    approved = models.BooleanField(default=False)
    objects=models.Manager()

    class Meta:
        db_table='teacher'
        verbose_name = 'Teacher'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name;

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class NotificationTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

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


    class Meta:
        db_table='paper'
        verbose_name = 'Test paper'
        verbose_name_plural=verbose_name
    
    def __str__(self):
        return self.Major;


class Grade(models.Model):
    sid = models.ForeignKey (Student, on_delete = models.CASCADE, default = '') # Add foreign key
    subject = models.CharField ('Subject',max_length = 20, default = '')
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.sid,self.grade);

    class Meta:
        db_table='grade'
        verbose_name = 'Achievement'
        verbose_name_plural=verbose_name