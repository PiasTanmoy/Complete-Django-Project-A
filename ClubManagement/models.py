from django.db import models

# Create your models here.


class Club(models.Model):

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/logo/')

    constitution = models.FileField(upload_to='files/constitution/')

    def __str__(self):
        return self.name