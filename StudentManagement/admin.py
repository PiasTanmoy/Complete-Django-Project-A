from django.contrib import admin
from .models import Student, Student_Course

# Register your models here.
admin.site.register( [Student, Student_Course] )

