from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=80)
    address = models.CharField(max_length=255)
    image=models.ImageField(upload_to='media/user')

    def __str__(self):
        return self.user.username