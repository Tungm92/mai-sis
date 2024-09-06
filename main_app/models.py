from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Staffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.BooleanField()
    administrator = models.BooleanField()
    dean = models.BooleanField()
    counselor = models.BooleanField()

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('staffer-detail', kwargs={'staffer_id':self.id})

    
class Student(models.Model):
    last_name = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    grade = models.IntegerField()
    iep = models.BooleanField()
    plan504 = models.BooleanField()
    eld = models.BooleanField() # how to make an enum?

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'student_id':self.id})

    
class Course(models.Model):
    instructor = models.ForeignKey(Staffer, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=24)
    subject = models.CharField(max_length=24) # how to make this a drop-down?
    credits = models.FloatField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'course_id':self.id})