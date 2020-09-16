from django.db import models
from StudentManagement.models import Student
# Create your models here.


class Address(models.Model):
    house_no = models.IntegerField()
    street_address = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return self.student.name
