from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

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
        messages.error(request, "FAÇA LOGIN OU CADASTRE-SE PARA ENTRAR NO SISTEMA.")
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
            return HttpResponse("ESTE LIVRO NÃO É SEU.")

    return redirect("login")


def register_book(request):
    if request.method == "POST":
        form_book = RegisterBook(request.POST)

        if form_book.is_valid():
            form_book.save()
            messages.success(request, "LIVRO CADASTRADO COM SUCESSO!")
            return redirect("home")
        else:
            messages.error(request, "DADOS INVÁLIDOS!")
            print(form_book)
            return redirect("home")


def del_book(request, id):
    book = Book.objects.get(id=id).delete()
    messages.error(request, "lIVRO DELETADO COM SUCESSO!")
    return redirect("home")


def register_category(request):
    form = RegisterCategory(request.POST)
    name = form.data["name"]
    id_user = request.POST.get("user")

    if int(id_user) == int(request.session.get("user")):
        user = User.objects.get(id=id_user)
        category = Category(name=name, user=user)
        category.save()
        messages.success(request, "CATEGORIA CADASTRADA COM SUCESSO!")
        return redirect("home")
    else:
        messages.error(request, "ERRO AO CADASTRAR CATEGORIA!")
        return redirect("home")


def register_borrowing(request):
    if request.method == "POST":
        form = RegisterBorrowing(request.POST)
        if form.is_valid():
            form.save()
            book_borrowed = form.data["book"]
            book = Book.objects.get(id=book_borrowed)
            if book.borrowed == False:
                book.borrowed = True
                book.save()
                messages.success(request, "EMPRÉSTIMO CADASTRADO.")
                return redirect("home")

            else:
                messages.error(
                    request, "ERRO AO CADASTRAR EMPRÉSTIMO. O LIVRO JÁ ESTÁ EMPRESTADO."
                )
                return redirect("home")
            
            
def return_book(request, id):
    book = Book.objects.get(id=id)
    if book.borrowed == False:
        messages.error(request, "O LIVRO NÃO ESTÁ EMPRESTADO.")
        return redirect("home")
    else:
        book.borrowed = False
        book.save()      
        borrowing = Borrowing.objects.get(Q(book=book) & Q(date_devolution=None))  
        borrowing.date_devolution = date.today()
        borrowing.save()
        
        messages.success(request, "LIVRO DEVOLVIDO.")
        return redirect("home")
