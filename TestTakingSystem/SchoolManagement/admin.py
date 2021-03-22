from django.contrib import admin

from .models import Student, Teacher, Subject, UserManager,Question,Grade,Paper, Courses,SessionYearModel
from .models import Student, Teacher, Subject, UserManager,Question,Grade,Paper
# Register your models here.

admin.site.register(Subject)
admin.site.register(UserManager)
admin.site.register(Paper)
admin.site.register(Courses)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','optionA','optionB','optionC','optionD','answer','level','score')
 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','admin','gender','address','birth')
    list_display_links = ('id','admin')

@admin.register(SessionYearModel)
class SessionYearModelAdmin(admin.ModelAdmin):
    list_display = ('id','session_start_year','session_end_year')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('sid','subject','grade')
