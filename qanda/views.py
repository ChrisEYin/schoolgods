from django.http import HttpResponse
from qanda.models import Department, Course, Professor, Question, Answer
from django.shortcuts import render_to_response

def index(request):
	a     = Department.objects.all()
	b     = Course.objects.all()
	c     = Professor.objects.all()
	return render_to_response('qanda/index.html', {'departments': a, 'courses': b, 'professors':c})
	
def courses(request, department_id):	
	a = Department.objects.get(pk = department_id)
	b = Course.objects.filter(department = a)
	return render_to_response('qanda/courses.html', {'department':a,'courses':b})
	
def professors(request, department_id, course_id):
	a = Department.objects.get(pk = department_id)
	b = Course.objects.filter(department = a)
	c = Course.objects.get(pk = course_id)
	d = Professor.objects.filter(course = course_id)
	return render_to_response('qanda/professors.html', {'department':a, 'course':b, 'course':c, 'professors':d})
	
def questions(request, department_id, course_id, professor_id):
	a = Department.objects.get(pk = department_id)
	b = Course.objects.filter(department = a)
	c = Course.objects.get(pk = course_id)
	d = Professor.objects.filter(course = course_id)
	e = Professor.objects.get(pk = professor_id)
	f = Question.objects.filter(professor = professor_id)
	return render_to_response('qanda/questions.html', {'department':a, 'course':b, 'course':c, 'professor':d, 'professor':e, 'questions':f})
	
def answers(request, department_id, course_id, professor_id, question_id):
	a = Department.objects.get(pk = department_id)
	b = Course.objects.filter(department = a)
	c = Course.objects.get(pk = course_id)
	d = Professor.objects.filter(course = course_id)
	e = Professor.objects.get(pk = professor_id)
	f = Question.objects.filter(professor = professor_id)
	g = Question.objects.get(pk = question_id)
	h = Answer.objects.filter(question = question_id)
	return render_to_response('qanda/answers.html', {'department':a, 'course':b, 'course':c, 'professor':d, 'professor':e, 'question':f, 'question':g, 'answers':h})	
	