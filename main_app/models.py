from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

GRADES = (
    ('k0', 'K0'),
    ('k1', 'K1'),
    ('k2', 'K2'),
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
    ('5', '5th'),
    ('6', '6th'),
    ('7', '7th'),
    ('8', '8th'),
    ('9', '9th'),
    ('10', '10th'),
    ('11', '11th'),
    ('12', '12th'),
)

ELDS = (
    ('N/A', 'Not applicable'),
    ('1', '1 - Entering'),
    ('2', '2 - Emerging'),
    ('3', '3 - Developing'),
    ('4', '4 - Expanding'),
    ('5', '5 - Bridging'),
    ('6', 'FLEP'),
)

SUBJECTS = (
    ('E', 'English Language Arts'),
    ('H', 'History'),
    ('M', 'Math'),
    ('S', 'Science'),
)

# Create your models here.
class Staffer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    grade = models.CharField(max_length=2, choices=GRADES, default=[0][0])
    iep = models.BooleanField('IEP')
    plan504 = models.BooleanField('504 Plan')
    eld = models.CharField('ELD', max_length=3, choices=ELDS, default=ELDS[0][0])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'student_id':self.id})

    
class Course(models.Model):
    instructor = models.ForeignKey(Staffer, on_delete=models.CASCADE)
    title = models.CharField(max_length=24)
    subject = models.CharField(max_length=1, choices=SUBJECTS, default=SUBJECTS[0][0])
    credits = models.FloatField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.title} -- {self.instructor} -- {self.get_subject_display()}'

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'course_id':self.id})