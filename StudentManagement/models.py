from django.db import models
from FacultyManagement.models import Advisor
from CourseManagement.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    contact_no = models.IntegerField(blank=True, null=True)

    advisor = models.ForeignKey(Advisor, on_delete=models.SET_DEFAULT, default=1)

    # s_id = models.IntegerField(unique=True)
    # id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Student_Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.student.name + " : " + self.course.code


