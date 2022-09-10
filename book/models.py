from django.db import models
from datetime import date

from user.models import User


class Category(models.Model):
    name = models.CharField("Nome", max_length=30)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Usuário",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Categoria"

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField("Nome", max_length=80)
    author = models.CharField("Autor", max_length=50)
    co_author = models.CharField("Co-autor", max_length=50, blank=True)
    registration_date = models.DateField("Data de cadastro", default=date.today)
    borrowed = models.BooleanField("Emprestado", default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Categoria",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Usuário",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Livro"

    def __str__(self) -> str:
        return self.name


class Borrowing(models.Model):
    username = models.CharField("Nome do Usuário", max_length=50)
    date_borrowed = models.DateField("Data de empéstimo", default=date.today)
    date_devolution = models.DateField("Data de devolução", blank=True, null=True)
    # time_duration = models.DateField(blank=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL, verbose_name="Livro", blank=True, null=True
    )

    class Meta:
        verbose_name = "Empréstimo"

    def __str__(self) -> str:
        return f"{self.username} | {self.book}"
