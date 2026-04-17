from django.db import models #models is a module in django orm object relatoional mapping
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    district = models.CharField(max_length=50, null=True, blank=True)

class Profilemodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile/')

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post = models.ImageField(upload_to='post/')

    
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_users')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
