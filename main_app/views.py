from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Staffer, Course, Student

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def staff_index(request):
    staff = Staffer.objects.all()
    return render(request, 'staff/index.html', { 'staff':staff })

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