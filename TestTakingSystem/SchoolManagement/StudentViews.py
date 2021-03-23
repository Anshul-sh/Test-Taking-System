import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from SchoolManagement.models import Student, Courses, Subject,UserManager, Paper


def student_home(request):
    print(request.user.id)
    student_obj=Student.objects.get(admin=request.user.id)
    course=Courses.objects.get(id=student_obj.id)
    subjects=Subject.objects.filter(course_id=course.id).count()
    subject_data=Subject.objects.filter(course_id=course.id)
    return render(request,"student_template/student_home_template.html",{"course":course,"subjects":subjects,"subject_name":subject_data})

def student_profile(request):
    user=UserManager.objects.get(id=request.user.id)
    print(user)
    student=Student.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))

def student_all_notification(request):
    student=Student.objects.get(admin=request.user.id)
    return render(request,"student_template/all_notification.html")

def student_view_result(request):
    student=Student.objects.get(admin=request.user.id)
    return render(request,"student_template/student_result.html")

def student_takeExam(request,subject_id):
    student=Student.objects.get(admin=request.user.id)
    subject = Subject.objects.get(id = subject_id)
    paper= Paper.objects.filter(subject=subject)
    return render(request,'exam.html',{'student':student,'paper':paper,'subject':subject})


def show_grade(request):
    messages.success(request, 'Form submission successful')
    return render(request,"student_template/student_result.html")
