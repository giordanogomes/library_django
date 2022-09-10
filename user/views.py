from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hashlib import sha256

from .models import User
from .forms import CaptchaTestForm


def login(request):
    if request.session.get("user"):
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        password = sha256(password.encode()).hexdigest()
        user = User.objects.filter(email=email).filter(password=password)

        captcha = CaptchaTestForm(request.POST)
        if captcha.is_valid():
            human = True
        else:
            messages.error(request, "CAPTCHA INCORRETO!")
            return redirect("login") 
           
        if len(user) == 0:
            messages.error(request, "EMAIL OU SENHA INCORRETOS!")
            return redirect("login")
        elif len(user) > 0:
            request.session["user"] = user[0].id
            messages.success(request, "USUÁRIO LOGADO.")
            return redirect("home")            
        
    captcha = CaptchaTestForm()
    return render(request, "login.html", {"captcha": captcha})


def register(request):
    if request.session.get("user"):
        return redirect("home")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email=email)
        
        captcha = CaptchaTestForm(request.POST)
        if captcha.is_valid():
            human = True
        else:
            messages.error(request, "CAPTCHA INCORRETO!")
            return redirect("register")
        
        if len(name.strip()) == 0 or len(email.strip()) == 0:
            messages.error(request, "OS CAMPOS DE NOME E EMAIL NÃO PODEM ESTAR VAZIOS!")
            return redirect("register")

        if len(user) > 0:
            messages.error(request, "USUÁRIO JÁ EXISTE!")
            return redirect("register")

        if len(password) < 8:
            messages.error(request, "A SENHA DEVE TER 8 OU MAIS CARACTERES!")
            return redirect("register")                            
        
        try:
            password = sha256(password.encode()).hexdigest()
            user = User(name=name, email=email, password=password)
            user.save()
            messages.success(request, "USUÁRIO CADASTRADO COM SUCESSO!")
            return redirect("login")
        except:
            messages.error(request, "ERRO INTERNO NO SISTEMA")
            return redirect("register")            

    captcha = CaptchaTestForm()
    return render(request, "register.html", {"captcha": captcha})


def logout(request):
    request.session.flush()
    return redirect("login")
