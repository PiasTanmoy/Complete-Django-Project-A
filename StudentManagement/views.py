from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def showStudents(request):
    studentList = Student.objects.all()
    context = {
        'students' : studentList
    }
    return render(request, 'StudentManagement/studentlist.html', context)



@login_required
def insertStudent(request):


    message = ""
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Student is inserted to DB. You can insert a new student now"
            form = StudentForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'StudentManagement/insertStudent.html', context)