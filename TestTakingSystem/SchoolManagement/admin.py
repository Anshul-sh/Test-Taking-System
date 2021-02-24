from django.contrib import admin

from .models import Student, Teacher, Subject, UserManager,Role
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(UserManager)
admin.site.register(Role)