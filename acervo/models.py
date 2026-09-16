from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Acervo(models.Model):
    livro.models.ManyToManyField("Livros", verbose_name="Acervo")
    type.models.CharField(Role.choice)

class Type(models.TextChoices):
    DIGITAL = "D1"
    FISICO = "F2"

class Category(models.IntegerChoices):
    
