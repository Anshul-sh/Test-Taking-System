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
    path('register/',SMViews.RegistrationView.as_view(),name= 'register'),
    #path('userCreater/',)
    url(r'^login/$', SMViews.login, name='login'),
    url(r'^home/$', SMViews.home, name='home'),
    url(r'^support/$', SMViews.support, name='support'),

    path('student_home', StudentViews.student_home, name="student_home"),
    url(r'^startExam/$',SMViews.startExam),

    # TODO 1: Create the URL for login
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)