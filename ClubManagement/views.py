from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import Club
from .forms import ClubForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def showClub(request):
    clubList = Club.objects.all()
    context = {
        'clubs' : clubList
    }
    return render(request, 'ClubManagement/viewClub.html', context)


@login_required
def insertClub(request):
    message = ""
    form = ClubForm()

    if request.method == "POST":
        form = ClubForm(request.POST, request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Club is inserted to DB. You can insert a new Club now"
            form = ClubForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'ClubManagement/registerClub.html', context)

