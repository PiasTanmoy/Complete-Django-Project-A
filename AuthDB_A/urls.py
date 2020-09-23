"""AuthDB_A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StudentManagement import views as student_views
from UserManagement import views as user_views
from ClubManagement import views as club_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_views.showStudents,  name='students'),
    path('insertstudent/', student_views.insertStudent, name='insertstudent'),
    path('registration/', user_views.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('clubs/', club_views.showClub, name='clubs'),
    path('insertclub/', club_views.insertClub, name='insert-club'),

    path('profile/', user_views.showProfile, name='profile'),
    path('createProfile/', user_views.createProfile, name='create-profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


