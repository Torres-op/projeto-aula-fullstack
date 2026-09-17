from django.db import models
from django.utils.translation import gettext_lazy as _

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Acervo(models.Model):

    class Type(models.TextChoices):
        DIGITAL = "D1"
        FISICO = "F2"

    class Category(models.IntegerChoices):
        GENERALIDADES_E_INFORMACOES = 0, _(
            "Generalidades e Informação: Obras gerais, enciclopédias, jornais e biblioteconomia."
        )

        FILOSOFIA_E_PSICOLOGIA = 100, _(
            "Filosofia e Psicologia: Ética, lógica e investigações sobre a mente humana."
        )

        RELIGIAO_E_TECNOLOGIA = 200, _(
            "Religião e Teologia: Mitologia, teologia e estudos sobre crenças e religiões."
        )

        CIENCIAS_SOCIAIS_E_DIREITO = 300, _(
            "Ciências Sociais e Direito: Política, economia, sociologia, educação e leis."
        )

        LINGUISTICA_E_IDIOMAS = 400, _(
            "Linguística e Idiomas: Gramáticas, dicionários e estudos de línguas."
        )

        CIENCIAS_PURAS = 500, _(
            "Ciências Puras (Exatas e Naturais): Matemática, física, química, biologia e astronomia."
        )

        CIENCIAS_APLICADAS = 600, _(
            "Ciências Aplicadas (Tecnologia): Medicina, engenharia, agricultura e administração."
        )

        ARTES_E_RECREACAO = 700, _(
            "Artes e Recreação: Pintura, música, arquitetura, esportes e lazer."
        )

        LITERATURA = 800, _(
            "Literatura: Poesia, romances, contos, crônicas e crítica literária."
        )

        HISTORIA_E_GEOGRAFIA = 900, _(
            "História e Geografia: Biografias, viagens e acontecimentos históricos."
        )


    categoria = models.IntegerField(
        choices=Category.choices,
        default=Category.GENERALIDADES_E_INFORMACOES,
        verbose_name="Categoria"
    )

    livro = models.ManyToManyField(Livro, verbose_name= _("livro"))

    tipo = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.DIGITAL,
        verbose_name="Tipo"
    )

