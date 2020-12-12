from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    college_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    address=models.TextField()
    mobile_no=models.CharField(max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
# Create your models here.
