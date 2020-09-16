from django.db import models

# Create your models here.

class Advisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    contact_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


