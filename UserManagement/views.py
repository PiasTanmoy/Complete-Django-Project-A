from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'UserManagement/registration.html', context)


from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def showProfile(request):
    ProfileList = Profile.objects.all()
    context = {
        'Profiles' : ProfileList
    }
    return render(request, 'UserManagement/viewProfile.html', context)


@login_required
def createProfile(request):
    message = ""
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():

            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            message = "Profile is inserted to DB. You can insert a new Profile now"
            form = ProfileForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'UserManagement/createProfile.html', context)

