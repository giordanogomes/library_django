from django.urls import path

from .views import login, register, validate_login, validate_register, logout

urlpatterns = [
    path("login/", login, name="login"),
    path("cadastro/", register, name="register"),
    path("validar_cadastro/", validate_register, name="validate_register"),
    path("validar_login/", validate_login, name="validate_login"),
    path("logout/", logout, name="logout"),
]
