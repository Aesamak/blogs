from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=150)
    blog=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='media/blog')
    author=models.ForeignKey(User,on_delete=models.CASCADE)