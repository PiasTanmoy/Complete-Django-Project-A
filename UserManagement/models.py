from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    cv = models.FileField(upload_to='files/cv')
    profile_picture = models.ImageField(upload_to='images/pro_pic')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
