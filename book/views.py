from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from user.models import User
from .models import Book, Borrowing, Category


def home(request):
    if request.session.get("user"):
        user = User.objects.get(id=request.session["user"])
        books = Book.objects.filter(user=user)
        return render(request, "home.html", {"books": books})
    else:
        messages.error(request, "LOGIN TO ENTER THE SYSTEM.")
        return redirect("/user/login/")


def info_book(request, id):
    if request.session.get("user"):
        book = Book.objects.get(id=id)
        if request.session.get("user") == book.user.id:
            category_book = Category.objects.filter(user_id=request.session.get("user"))
            borrowing = Borrowing.objects.filter(book=book)
            return render(
                request,
                "info_book.html",
                {"book": book, "category_book": category_book, "borrowing": borrowing},
            )
        else:
            return HttpResponse("This book is not yours")

    return redirect("user/login/")
