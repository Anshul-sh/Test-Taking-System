"""TestTakingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from TestTakingSystem import settings
from django.conf.urls.static import static
import SchoolManagement.views as SMViews
from SchoolManagement import StudentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # Homepage inside the School Management System 
    path('', SMViews.home),
    path('face_detection/',SMViews.FaceDetection.as_view(),name = 'face_detection'),
    path('student_registration/',SMViews.CreateStudent ,name = 'register'),
    #path('<slug:pk>/student_registration/', SMViews.StudentRegistration.as_view(), name="student_registration"),
    url(r'^login/$', SMViews.login, name='login'),
    path('login/', SMViews.login, name='login'),
    path('face_id/', SMViews.FaceId.as_view(),name='face_id'),
    path('profile/',SMViews.Profile.as_view(),name='profile'),
    url(r'^home/$', SMViews.home, name='home'),
    url(r'^support/$', SMViews.support, name='support'),
    path('logout_user', SMViews.logout_user,name="logout"),

    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path('student_all_notification',StudentViews.student_all_notification,name="student_all_notification"),
    path('student_view_result',StudentViews.student_view_result,name="student_view_result"),

    url(r'^startExam/$',SMViews.startExam),

    # TODO 1: Create the URL for login
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)