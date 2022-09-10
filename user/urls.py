from django.urls import path

from .views import login, register, logout

urlpatterns = [
    path("login/", login, name="login"),
    path("cadastro/", register, name="register"),    
    path("logout/", logout, name="logout"),
]
