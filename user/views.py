from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hashlib import sha256

from .models import User


def login(request):
    if request.session.get("user"):
        return redirect("/book/home/")

    return render(request, "login.html")


def register(request):
    if request.session.get("user"):
        return redirect("/book/home/")

    return render(request, "register.html")


def validate_register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")

    user = User.objects.filter(email=email)

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        messages.error(request, "THE NAME AND EMAIL FIELDS CANNOT BE EMPTY!")
        return redirect("/user/register/")

    if len(user) > 0:
        messages.error(request, "USER ALREADY EXISTS!")
        return redirect("/user/register/")

    if len(password) < 8:
        messages.error(request, "PASSWORD MUST BE 8 OR MORE CHARACTERS!")
        return redirect("/user/register/")

    try:
        password = sha256(password.encode()).hexdigest()
        user = User(name=name, email=email, password=password)
        user.save()
        messages.success(request, "USER REGISTERED SUCCESSFULLY!")
        return redirect("/user/login/")
    except:
        messages.error(request, "INTERNAL SYSTEM ERROR")
        return redirect("/user/register/")


def validate_login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    password = sha256(password.encode()).hexdigest()
    user = User.objects.filter(email=email).filter(password=password)

    if len(user) == 0:
        messages.error(request, "INCORRECT EMAIL OR PASSWORD!")
        return render(request, "login.html")
    elif len(user) > 0:
        request.session["user"] = user[0].id
        return redirect("/book/home/")

    return HttpResponse(f"{email} - {password}")


def logout(request):
    request.session.flush()
    return redirect("/user/login/")
