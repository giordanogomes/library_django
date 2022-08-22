from django import forms

from .models import Book


class RegisterBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # ("name", "author", "co_author", "registration_date", "category")
