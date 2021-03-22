from django.contrib import admin

from .models import Student, Teacher, Subject, UserManager,Question,Grade,Paper, Courses,SessionYearModel
from .models import Student, Teacher, Subject, UserManager,Question,Grade,Paper
# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(UserManager)
admin.site.register(Grade)
admin.site.register(Paper)
admin.site.register(Courses)
admin.site.register(SessionYearModel)
admin.site.register(Question)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name']

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','level','score')
 