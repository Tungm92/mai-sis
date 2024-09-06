from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = False
    admininistrator = False
    dean = False
    counselor = False

    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    last_name = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    grade = models.IntegerField()
    iep = models.BooleanField()
    plan504 = models.BooleanField()
    eld = models.BooleanField() # how to make an enum?

    def __str__(self):
        return self.first_name

    
class Course(models.Model):
    instructor = models.ForeignKey(Staffer, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=24)
    subject = models.CharField(max_length=24) # how to make this a drop-down?
    credits = models.FloatField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_title
