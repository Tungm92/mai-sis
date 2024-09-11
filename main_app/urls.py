from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('staff/', views.staff_index, name='staff-index'),    
    path('staff/<int:staffer_id>/', views.staff_detail, name='staffer-detail'),
    path('staff/create/', views.StafferCreate.as_view(), name='staffer-create'),
    path('staff/<int:pk>/update/', views.StafferUpdate.as_view(), name='staffer-update'),
    path('staff/<int:pk>/delete/', views.StafferDelete.as_view(), name='staffer-delete'),
    path('students/', views.students_index, name='student-index'),
    path('students/<int:student_id>/', views.student_detail, name='student-detail'),
    path('students/create/', views.StudentCreate.as_view(), name='student-create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),
    path('students/<int:student_id>/associate-course/<int:course_id>/', views.associate_course, name='associate-course'),
    path('students/<int:student_id>/remove-course/<int:course_id>/', views.remove_course, name='remove-course'),
    path('courses/', views.courses_index, name='course-index'),
    path('courses/<int:course_id>/', views.course_detail, name='course-detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', views.CourseUpdate.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='course-delete'),
    path('courses/<int:course_id>/associate-student/<int:student_id>/', views.associate_student, name='associate-student'),
    path('courses/<int:course_id>/remove-student/<int:student_id>/', views.remove_student, name='remove-student'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
