from django.shortcuts import redirect, render
from .models import Livro, Acervo
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all() # busca no banco
    return render(
        request, 'acervo/lista.html',
        {'livros': livros} # envia ao template
    )
    
def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save() # grava no banco
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})   

def listar_acervo(request):
    nome = request.GET.get("nome", "").strip()
    tipo = request.GET.get("tipo", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    acervos = Acervo.objects.all().prefetch_related("livro")

    if nome:
        acervos = acervos.filter(
            livro__titulo__icontains=nome
        )

    if tipo:
        acervos = acervos.filter(tipo=tipo)

    if categoria.isdigit():
        acervos = acervos.filter(categoria=categoria)

    acervos = acervos.distinct()

    context = {
        "acervos": acervos,
        "tipos": Acervo.Type.choices,
        "categorias": Acervo.Category.choices,

        "nome": nome,
        "tipo_selecionado": tipo,
        "categoria_selecionada": categoria,
    }

    return render(
        request,
        "acervo/listar.html",
        context
    )