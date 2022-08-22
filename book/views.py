from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from user.models import User
from .models import Book, Borrowing, Category
from .forms import RegisterBook


def home(request):
    if request.session.get("user"):
        user = User.objects.get(id=request.session["user"])
        books = Book.objects.filter(user=user)
        form = RegisterBook()
        return render(
            request,
            "home.html",
            {
                "books": books,
                "logged_user": request.session.get("user"),
                "form": form,
            },
        )
    else:
        messages.error(request, "LOGIN TO ENTER THE SYSTEM.")
        return redirect("/user/login/")


def info_book(request, id):
    if request.session.get("user"):
        book = Book.objects.get(id=id)
        if request.session.get("user") == book.user.id:
            category_book = Category.objects.filter(user_id=request.session.get("user"))
            borrowing = Borrowing.objects.filter(book=book)
            form = RegisterBook()
            return render(
                request,
                "info_book.html",
                {
                    "book": book,
                    "category_book": category_book,
                    "borrowing": borrowing,
                    "logged_user": request.session.get("user"),
                    "form": form,
                },
            )
        else:
            return HttpResponse("This book is not yours")

    return redirect("/user/login/")


def register_book(request):
    if request.method == "POST":
        form = RegisterBook(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "dados salvos com sucesso.")
            return redirect("/book/home/")
        else:
            return HttpResponse("dados invalidos")
