from django.db import models


class User(models.Model):
    name = models.CharField("Nome", max_length=40)
    email = models.EmailField("Email")
    password = models.CharField("Senha", max_length=64)

    class Meta:
        verbose_name = "Usuário"

    def __str__(self) -> str:
        return self.name
