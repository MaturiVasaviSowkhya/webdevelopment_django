from django.db import models

# Create your models here.
class Student(models.Model):
	genders = [('Female','Female'),
				('male','male'),
				('others','others')]
	fname = models.CharField(max_length = 25)
	lname = models.CharField(max_length = 15)
	name = models.CharField(max_length = 35)
	rnum = models.CharField(max_length = 28)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	gender = models.CharField(max_length = 15,choices = genders)
	age = models.IntegerField(null = True)

	def __str__(self):
		return self.name + ' ' + self.email