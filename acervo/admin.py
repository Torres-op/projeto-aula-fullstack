from django.contrib import admin
from .models import Livro, Acervo

class AcervoAdmin(admin.ModelAdmin):
    list_filter = ['tipo', 'categoria']
    search_fields = ['livro__titulo']

admin.site.register(Livro)
admin.site.register(Acervo, AcervoAdmin)