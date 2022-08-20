from django.urls import path

from .views import home, info_book

urlpatterns = [
    path("home/", home),
    path("info_book/<int:id>", info_book, name="info_book"),
]
