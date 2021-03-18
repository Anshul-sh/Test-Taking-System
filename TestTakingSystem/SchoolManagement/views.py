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
# import face_recognition
import cv2 
#from SchoolManagement.serializer import ImageSerializer
from rest_framework.response import Response
from urllib import request as url_request
from SchoolManagement import models

from SchoolManagement.forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from SchoolManagement.models import Student, Paper
from django.urls import reverse_lazy

# import views types
from django.views.generic.edit import CreateView


from django.contrib import messages

def home(request):
    return render(request,'main/base.html',{})

class FaceDetection(APIView):
    def get(self, request):
        return render(request, 'face_detection.html')



class RegistrationView(CreateView):
    model = UserManager
    fields = ['email','first_name','last_name','username','password','user_role']
    template_name = 'register.html'
    success_url = reverse_lazy('')
    def form_valid(self, form):    
        user = form.save(commit=False)
        role = user.user_role
        user.save()
        # Add action to valid form phase
        if(role == 'Student'):
            messages.success(self.request, 'Student redirect')
            return HttpResponseRedirect(self.get_success_url())  
        elif(role == 'Staff'):
            return HttpResponseRedirect(self.get_success_url()) 


# class faceid(APIView):
    #serializer_class = ImageSerializer
    #permission_classes = [AllowAny]
    # def post(self, request):
    #     loc = '\\images\\stored\\test2.jpg'
    #     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     MEDIA_ROOT =os.path.join(BASE_DIR,'SchoolManagement')
    #     uri  = request.POST.__getitem__('image')
    #     with url_request.urlopen(uri) as resp:
    #         with open((str(MEDIA_ROOT)+'\\images\\image.jpg'), 'wb') as f:
    #             f.write(resp.file.read())
    #     img = cv2.imread((str(MEDIA_ROOT)+'\\images\\image.jpg'),1)

#         print(MEDIA_ROOT,loc)
#         loc=(str(MEDIA_ROOT)+loc)
#         print(loc)

#         print("/images/stored/test.jpg")
#         face_1_image = face_recognition.load_image_file(loc)
#         face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]


#         small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
#         rgb_small_frame = small_frame[:, :, ::-1]

#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)

#         print(check)
#         if check[0]:
#                 return True
        
#         else :
#                 return False
#     def get(self, request):
#         return render(request ,'faceid.html')

@login_required
class profile(APIView):
    template_name = 'profile.html'
    def get(self, request):
        # queryset = UserManager.get('self')
        return HttpResponseRedirect(reverse("student_home"))

        # return Response({'profile': queryset})


def support(request):
    return render(request,'main/base.html',{})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                 return profile(request)
            
            if user is not None: 
                profile(request, user)

            else: 
                return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
        else: 
            return HttpResponse('<p> User name or password is incorrect. Please try again.</p>')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def startExam(request):
    sid = request.GET.get('sid')
    subject1=request.GET.get('subject')

    student=models.Student.objects.get(id=sid)
    paper= models.Paper.objects.filter(subject=subject1)
    return render(request,'exam.html',{'student':student,'paper':paper,'subject':subject1})
