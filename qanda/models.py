import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
	subject         = models.CharField(max_length = 25)
	pub_date        = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.subject
		
class Course(models.Model):
	department      = models.ForeignKey(Department)
	number          = models.CharField(max_length = 50)
	name            = models.CharField(max_length = 100, blank = True, null = True)
	pub_date        = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.number
	
class Professor(models.Model):
	course          = models.ForeignKey(Course)
	name            = models.CharField(max_length = 50)
	pub_date        = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.name
	
class Question(models.Model):
	professor       = models.ForeignKey(Professor, blank = True, null = True)
	question_text   = models.CharField(max_length = 500)
	question_detail = models.CharField(max_length = 1000)
	q_pub_date      = models.DateTimeField(auto_now_add = True)
	q_author        = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.question_text
		
class Answer(models.Model):
	question        = models.ForeignKey(Question, blank = True, null = True)
	answer_text     = models.CharField(max_length = 10000)
	a_pub_date      = models.DateTimeField(auto_now_add = True)
	a_author        = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.answer_text
	
