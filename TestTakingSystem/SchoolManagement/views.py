from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from SchoolManagement.models import Student,UserManager
import os
from django.urls import path, include
import face_recognition
import cv2 
from SchoolManagement.serializer import ImageSerializer
from rest_framework.response import Response
# Create your views here.

# TODO 1: Create the base templeate

# Home page for the complete Website 
def home(request):
    return render(request,'main\\base.html',{})
# TODO 2: Code for login


class faceid(APIView):
    serializer_class = ImageSerializer
    #permission_classes = [AllowAny]
    def post(self, request):
        print(request)
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # MEDIA_ROOT =os.path.join(BASE_DIR,'pages')

        # print(MEDIA_ROOT,loc)
        # loc=(str(MEDIA_ROOT)+loc)
        # print(loc)
        # print("/home/light/codes/web/djangoproject/mysite/pages/media/profil_images/IMG_20180330_1600482-01.jpg")
        # face_1_image = face_recognition.load_image_file(loc)
        # face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

        # #

        # small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        # rgb_small_frame = small_frame[:, :, ::-1]

        # face_locations = face_recognition.face_locations(rgb_small_frame)
        # face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)

        # print(check)
        # if check[0]:
        #         return True
        
        # else :
        #         return False
    def get(self, request):
        return render(request ,'faceid.html')


@login_required
class profile(APIView):
    template_name = 'profile.html'

    def get(self, request):
        queryset = UserManager.get('self')
        return Response({'profile': queryset})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                return profile(request)
                
            else: 
                return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
        else: 
            return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Face Varification Page
@login_required
def faceVarification(request):
    return HttpResponce("<p>Testing</p>")