from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Hàm tạo profile cho tài khoản
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} Profile'