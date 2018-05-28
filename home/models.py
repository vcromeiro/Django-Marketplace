from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)
        
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
        
class Product(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    price = models.IntegerField(blank=True, null=True)
    image = models.FileField(upload_to='product_image', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)