from django.contrib import admin
from qanda.models import Department, Course, Professor, Question, Answer

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('subject', 'pub_date')
	
class CourseAdmin(admin.ModelAdmin):
	list_display = ('department', 'number', 'name', 'pub_date')

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('course', 'name', 'pub_date')
	
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('professor', 'question_text', 'question_detail', 'q_author')
	
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('question', 'answer_text', 'a_author')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)