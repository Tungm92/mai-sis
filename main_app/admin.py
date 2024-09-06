from django.contrib import admin
from .models import Staffer, Course, Student

# Register your models here.
admin.site.register(Staffer)
admin.site.register(Course)
admin.site.register(Student)