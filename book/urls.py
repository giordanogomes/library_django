from django.urls import path

from .views import home, info_book, register_book, del_book, register_category

urlpatterns = [
    path("home/", home, name="home"),
    path("info_book/<int:id>", info_book, name="info_book"),
    path("register_book/", register_book, name="register_book"),
    path("del_book/<int:id>", del_book, name="del_book"),
    path("registe_category/", register_category, name="register_category"),
]
