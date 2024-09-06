from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete')
]
