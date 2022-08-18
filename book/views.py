from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from user.models import User
from .models import Book


def home(request):
    if request.session.get("user"):
        user = User.objects.get(id=request.session["user"])
        books = Book.objects.filter(user=user)
        return render(request, "home.html", {"books": books})
    else:
        messages.error(request, "FAÇA LOGIN PARA ENTRAR NO SISTEMA.")
        return redirect("/user/login/")


def info_book(request, id):
    book = Book.objects.get(id=id)
    
    return render(request, "info_book.html", {"book": book})
