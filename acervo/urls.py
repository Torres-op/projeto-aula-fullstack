from django.urls import path
from . import views

urlpatterns = [
    path(
        'livros/',
        views.lista_livros,
        name='lista'
    ),
    path(
        'livros/novo/',
        views.novo_livro,
        name='novo'
    ),
    path(
        'acervos/',
        views.listar_acervo,
        name='listar_acervo'
    ),
]