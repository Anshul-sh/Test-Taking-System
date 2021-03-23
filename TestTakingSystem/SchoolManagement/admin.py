from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Student, Teacher, Subject, UserManager, Course,SessionYearModel, Teacher, Quiz, MCQuestion, Answer ,Question ,Progress,NotificationTeacher
from django.utils.translation import ugettext_lazy as _

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer


class QuizAdminForm(forms.ModelForm):
    """
    below is from
    http://stackoverflow.com/questions/11657682/
    django-admin-interface-using-horizontal-filter-with-
    inline-manytomany-field
    """

    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial =\
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz


class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'Course', )
    list_filter = ('Course',)
    search_fields = ('description', 'Course', )


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('Course', )


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('Subject', )
    list_display = ('Subject', 'Course',)
    list_filter = ('Course',)


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'Course', )
    list_filter = ('Course',)
    fields = ('content', 'Course', 'Subject',
              'figure', 'quiz', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)

    inlines = [AnswerInline]


class ProgressAdmin(admin.ModelAdmin):
    """
    to do:
            create a user section
    """
    search_fields = ('user', 'score', )




admin.site.register(Student)
#admin.site.register(Subject)
admin.site.register(UserManager)
#admin.site.register(Quiz)
admin.site.register(Teacher)
#admin.site.register(Course)
admin.site.register(SessionYearModel)
admin.site.register(NotificationTeacher)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(Progress, ProgressAdmin)



# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'sex', 'password', 'email', 'birth')
#     list_display_links = ('id', 'name')
#     search_fields = ['name', 'dept', 'birth']
#     list_filter = ['name']

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','level','score')
 