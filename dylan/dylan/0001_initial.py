from blog.models import Post
from django.contrib.auth.models import User
User.Objects.all:()

# Select * from User;

from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)