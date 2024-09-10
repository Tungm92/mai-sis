from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Staffer, Course, Student
from django.contrib.auth.views import LoginView


# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def staff_index(request):
    staff = Staffer.objects.all()
    return render(request, 'staff/index.html', { 'staff':staff})

def staff_detail(request, staffer_id):
    staffer = Staffer.objects.get(id=staffer_id)
    return render(request, 'staff/detail.html', { 'staffer':staffer })

class StafferCreate(CreateView):
    model = Staffer
    fields = '__all__'

class StafferUpdate(UpdateView):
    model = Staffer
    fields = ['teacher', 'administrator', 'dean', 'counselor']

class StafferDelete(DeleteView):
    model = Staffer
    success_url = '/staff/'

def students_index(request):
    students = Student.objects.order_by('last_name')
    return render(request, 'students/index.html', { 'students':students })

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', { 'student':student })

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'grade', 'iep', 'plan504', 'eld']

class StudentDelete(DeleteView):
    model = Student
    success_url = '/students/'

def courses_index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', { 'courses':courses })

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students_not_on_roster = Student.objects.exclude(id__in = course.students.all().values_list('id'))
    return render(request, 'courses/detail.html', { 'course':course, 'students':students_not_on_roster })

class CourseCreate(CreateView):
    model = Course
    fields = ['instructor','title','subject','credits']

class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'

class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses/'

def associate_student(request, course_id, student_id):
    Course.objects.get(id=course_id).students.add(student_id)
    return redirect('course-detail', course_id=course_id)

def remove_student(request, course_id, student_id):
    course = Course.objects.get(id=course_id)
    course.students.remove(student_id)
    return redirect('course-detail', course_id=course_id)
