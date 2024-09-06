from django.shortcuts import render
from .models import Staffer, Course, Student

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def staff_index(request):
    staff = Staffer.objects.filter(user.request.user)
    return render(request, 'staff/index.html', { 'staff':staff })

# def staff_

def students_index(request):
    students = Student.objects.order_by('last_name')
    return render(request, 'students/index.html', { 'students':students })