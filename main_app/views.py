from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Staffer, Course, Student
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def staff_index(request):
    staff = Staffer.objects.all()
    return render(request, 'staff/index.html', { 'staff':staff})

@login_required
def staff_detail(request, staffer_id):
    staffer = Staffer.objects.get(id=staffer_id)
    courses = Course.objects.filter(instructor=staffer)
    return render(request, 'staff/detail.html', { 'staffer':staffer, 'courses':courses })

class StafferCreate(CreateView):
    model = Staffer
    fields = '__all__'

class StafferUpdate(UpdateView):
    model = Staffer
    fields = ['teacher', 'administrator', 'dean', 'counselor']

class StafferDelete(DeleteView):
    model = Staffer
    success_url = '/staff/'

@login_required
def students_index(request):
    students = Student.objects.order_by('last_name')
    return render(request, 'students/index.html', { 'students':students })

@login_required
def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    enrolled = Course.objects.filter(students=student_id)
    unenrolled = Course.objects.exclude(students=student_id)
    return render(request, 'students/detail.html', { 'student':student, 'enrolled':enrolled, 'unenrolled':unenrolled })

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'grade', 'iep', 'plan504', 'eld']

class StudentDelete(DeleteView):
    model = Student
    success_url = '/students/'

@login_required
def courses_index(request):
    courses = Course.objects.order_by('title')
    return render(request, 'courses/index.html', { 'courses':courses })

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    enrolled = course.students.order_by('last_name')
    students_not_on_roster = Student.objects.exclude(id__in = course.students.all().values_list('id')).order_by('last_name')
    return render(request, 'courses/detail.html', { 'course':course, 'students':students_not_on_roster, 'enrolled':enrolled })

class CourseCreate(CreateView):
    model = Course
    fields = ['instructor','title','subject','credits']

class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'

class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses/'

@login_required
def associate_student(request, course_id, student_id):
    Course.objects.get(id=course_id).students.add(student_id)
    return redirect('course-detail', course_id=course_id)

@login_required
def remove_student(request, course_id, student_id):
    course = Course.objects.get(id=course_id)
    course.students.remove(student_id)
    return redirect('course-detail', course_id=course_id)

@login_required
def associate_course(request, student_id, course_id):
    Course.objects.get(id=course_id).students.add(student_id)
    return redirect('student-detail', student_id=student_id)

@login_required
def remove_course(request, student_id, course_id):
    course = Course.objects.get(id=course_id)
    course.students.remove(student_id)
    return redirect('student-detail', student_id=student_id)