from django.urls import path

from .views import (
    home,
    info_book,
    register_book,
    del_book,
    register_category,
    register_borrowing,
    return_book,
)

urlpatterns = [
    path("", home, name="home"),
    path("info_livro/<int:id>", info_book, name="info_book"),
    path("cadastrar_livro/", register_book, name="register_book"),
    path("del_livro/<int:id>", del_book, name="del_book"),
    path("cadastrar_categoria/", register_category, name="register_category"),
    path("cadastrar_emprestimo/", register_borrowing, name="register_borrowing"),
    path("devolver_livro/<int:id>", return_book, name="return_book"),
]
