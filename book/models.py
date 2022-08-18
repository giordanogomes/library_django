from django.db import models
from datetime import date

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)    
    
    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    registration_date = models.DateField(default=date.today)
    rented = models.BooleanField(default=False)
    name_rented = models.CharField(max_length=50, blank=True, null=True)
    date_rented = models.DateTimeField(blank=True, null=True)
    date_devolution = models.DateTimeField(blank=True, null=True)
    time_duration = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name    
