from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hashlib import sha256

from .models import User

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def validate_register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = User.objects.filter(email=email)
    
    if len(name.strip()) == 0 or len(email.strip()) == 0:
        messages.error(request, 'OS CAMPOS NOME E EMAIL NÃO PODEM ESTAR VAZIOS!')
        return redirect('/user/register/')
    
    if len(user) > 0:        
        messages.error(request, 'USUÁRIO JÁ EXISTE!')
        return redirect('/user/register/')
    
    if len(password) < 8:
        messages.error(request, 'SENHA PRECISA TER 8 OU MAIS CARACTERES!')
        return redirect('/user/register/')
    
    try:
        password = sha256(password.encode()).hexdigest()
        user = User(name=name, email=email, password=password)
        user.save()
        messages.success(request, 'USUÁRIO CADASTRADO COM SUCESSO!')
        return redirect('/user/login/')
    except:
        messages.error(request, 'ERRO INTERNO DO SISTEMA')
        return redirect('/user/register/')   
    
def validate_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    password = sha256(password.encode()).hexdigest()
    user = User.objects.filter(email=email).filter(password=password)
    
    if len(user) == 0:
        messages.error(request, 'EMAIL OU SENHA INCORRETOS!')
        return render(request, 'login.html')
    elif len(user) > 0:
        request.session['user'] = user[0].id
        return redirect('/book/home/')
    
    return HttpResponse(f'{email} - {password}')

def logout(request):
    request.session.flush()
    return redirect('/user/login/')
