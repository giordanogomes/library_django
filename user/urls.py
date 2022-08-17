from django.urls import path

from .views import login, register, validate_login, validate_register, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('validate_register/', validate_register, name='validate_register'),
    path('validate_login/', validate_login, name='validate_login'),
    path('logout/', logout, name='logout'),
]
