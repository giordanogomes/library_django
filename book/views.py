from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from user.models import User
from .models import Book, Borrowing, Category
from .forms import RegisterBook, RegisterCategory, RegisterBorrowing


def home(request):
    if request.session.get("user"):
        user = User.objects.get(id=request.session["user"])
        books = Book.objects.filter(user=user)        
        form_book = RegisterBook()
        form_category = RegisterCategory()
        form_borrowing = RegisterBorrowing()
        
        form_book.fields["user"].initial = request.session["user"]
        form_book.fields["category"].queryset = Category.objects.filter(user=user)
        
        form_category.fields["user"].initial = request.session["user"]
        
        form_borrowing.fields["book"].queryset = Book.objects.filter(user=user)
        
        return render(
            request,
            "home.html",
            {
                "books": books,
                "logged_user": request.session.get("user"),
                "form_book": form_book,
                "form_category": form_category,
                "form_borrowing": form_borrowing,
            },
        )
    else:
        messages.error(request, "LOGIN TO ENTER THE SYSTEM.")
        return redirect("login")


def info_book(request, id):
    if request.session.get("user"):
        book = Book.objects.get(id=id)
        if request.session.get("user") == book.user.id:
            user = User.objects.get(id=request.session["user"])
            category_book = Category.objects.filter(user_id=request.session.get("user"))
            borrowing = Borrowing.objects.filter(book=book)
            form_book = RegisterBook()
            form_category = RegisterCategory()
            form_borrowing = RegisterBorrowing()
            
            form_book.fields["user"].initial = request.session["user"]
            form_book.fields["category"].queryset = Category.objects.filter(user=user)
            
            form_category.fields["user"].initial = request.session["user"]
            
            form_borrowing.fields["book"].queryset = Book.objects.filter(user=user)
            
            return render(
                request,
                "info_book.html",
                {
                    "book": book,
                    "category_book": category_book,
                    "borrowing": borrowing,
                    "logged_user": request.session.get("user"),
                    "form_book": form_book,
                    "id_book": id,
                    "form_category": form_category,
                    "form_borrowing": form_borrowing,
                },
            )
        else:
            return HttpResponse("THIS BOOK IS NOT YOURS.")

    return redirect("login")


def register_book(request):
    if request.method == "POST":
        form_book = RegisterBook(request.POST)
        
        if form_book.is_valid():
            form_book.save()
            messages.success(request, "REGISTERED BOOK.")
            return redirect("home")
        else:
            messages.error(request, "INVALID DATA.")
            return redirect("home")
        
        
def del_book(request, id):
    book = Book.objects.get(id=id).delete()
    messages.warning(request, "BOOK HAS BEEN DELETED!")
    return redirect("home")


def register_category(request):
    form = RegisterCategory(request.POST)
    name = form.data["name"]
    id_user = request.POST.get("user")
    
    if int(id_user) == int(request.session.get("user")):
        user = User.objects.get(id=id_user)
        category = Category(name=name, user=user)
        category.save()
        return HttpResponse("Success!")
    else:            
        return HttpResponse(f"ERROR!")
