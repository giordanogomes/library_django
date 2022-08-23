from django.db import models
from datetime import date

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    co_author = models.CharField(max_length=50, blank=True)
    registration_date = models.DateField(default=date.today)
    borrowed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


class Borrowing(models.Model):
    name_borrowed = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    name_borrowed_anonymous = models.CharField(max_length=50, blank=True, null=True)
    date_borrowed = models.DateField(blank=True, null=True)
    date_devolution = models.DateField(blank=True, null=True)
    # time_duration = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.name_borrowed} | {self.book}"
