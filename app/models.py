from django.db import models

# Create your models here.
class aman(models.Model):
    name=models.CharField(max_length=80)
    rollno=models.CharField(max_length=40)
    