from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from user.models import User

def home(request):
    if request.session.get('user'):
        user = User.objects.get(id=request.session['user']).name
        return HttpResponse(f'Eai {user} <br> Salve Ximba!')
    else:
        messages.error(request, 'FAÇA LOGIN PARA ENTRAR NO SISTEMA.')
        return redirect('/user/login/')
