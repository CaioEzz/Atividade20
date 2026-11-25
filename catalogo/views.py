from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Autor, Genero, Livro

LIVROS_POR_PAGINA = 5


def lista_livros(request):
    # 1. Parâmetros recebidos via GET (strings; vazias se não vieram na URL)
    busca = request.GET.get("q", "").strip()
    autor_id = request.GET.get("autor", "")
    genero_id = request.GET.get("genero", "")

    # 2. Consulta base. select_related faz JOIN e evita 1 consulta extra por livro
    livros = Livro.objects.select_related("autor", "genero").order_by("titulo")

    # 3. Filtros aplicados ANTES da paginação; cada um é opcional e eles se combinam
    if busca:
        livros = livros.filter(titulo__icontains=busca)
    if autor_id.isdigit():
        livros = livros.filter(autor_id=autor_id)
    if genero_id.isdigit():
        livros = livros.filter(genero_id=genero_id)

    # 4. Paginação: 5 registros por página
    paginator = Paginator(livros, LIVROS_POR_PAGINA)
    page_obj = paginator.get_page(request.GET.get("page"))

    # 5. Querystring sem "page", para preservar busca e filtros nos links
    params = request.GET.copy()
    params.pop("page", None)
    querystring = params.urlencode()

    contexto = {
        "page_obj": page_obj,
        "total_resultados": paginator.count,
        "autores": Autor.objects.all(),
        "generos": Genero.objects.all(),
        "busca": busca,
        "autor_sel": autor_id,
        "genero_sel": genero_id,
        "querystring": querystring,
    }
    return render(request, "catalogo/lista_livros.html", contexto)
