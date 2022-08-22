from django.urls import path

from .views import home, info_book, register_book

urlpatterns = [
    path("home/", home, name="home"),
    path("info_book/<int:id>", info_book, name="info_book"),
    path("register_book/", register_book, name="register_book"),
]
