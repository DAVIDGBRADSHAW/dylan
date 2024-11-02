from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('User', on_delete=models.CASCADE)

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)