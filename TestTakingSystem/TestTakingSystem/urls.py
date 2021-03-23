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


urlpatterns = [
    path('admin/', admin.site.urls),
    # Homepage inside the School Management System 
    path('',SMViews.home,name='home'),
    path('face_detection/',SMViews.FaceDetection.as_view(),name = 'face_detection'),
    path('student_registration/',SMViews.CreateStudent ,name = 'register'),
    path('login/', SMViews.login, name='login'),
    path('face_id/', SMViews.FaceId.as_view(),name='face_id'),
    path('profile/',SMViews.Profile.as_view(),name='profile'),
    path('logout/', SMViews.userlogout,name='logout'),
    path('staff_notification/',SMViews.staff_notification,name='staff_notification'),
    url(r'^support/$', SMViews.support, name='support'),
     url(r'^change_password/$', SMViews.change_password, name='change_password'),
    
    url(r'^quizlist/$',
        view=SMViews.QuizListView.as_view(),
        name='quiz_index'),
    url(r'^category/$',
        view=SMViews.CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    url(r'^category/(?P<category_name>[\w|\W-]+)/$',
        view=SMViews.ViewQuizListByCourse.as_view(),
        name='quiz_category_list_matching'),

    url(r'^progress/$',
        view=SMViews.QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(r'^quizmarking/$',
        view=SMViews.QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(r'^marking/(?P<pk>[\d.]+)/$',
        view=SMViews.QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url(r'^(?P<slug>[\w-]+)/$',
        view=SMViews.QuizDetailView.as_view(),
        name='quiz_start_page'),

    url(r'^(?P<quiz_name>[\w-]+)/take/$',
        view=SMViews.QuizTake.as_view(),
        name='quiz_question'),
    # TODO 1: Create the URL for login
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)