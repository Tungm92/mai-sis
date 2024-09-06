from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staff/', views.staff_index, name='staff-index'),    
    # path('staff/<int:staff_id>/', views.staff._detail, name='staff-detail'),
    # path('staff/create/', views.StaffCreate.as_view(), name='staff-create'),
    # path('staff/<int:pk>/update/', views.StaffUpdate.as_view(), name='staff-update'),
    # path('staff/<int:pk>/delete/', views.StaffDelete.as_view(), name='staff-delete'),
    path('students/', views.students_index, name='student-index'),

]
