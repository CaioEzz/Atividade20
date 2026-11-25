# 📚 Estante Viva — Catálogo de Livros

**Disciplina:** Programação para Internet
**Tecnologia:** Python + Django 5
**Tema escolhido:** Catálogo de Livros

## Integrantes da dupla
- Nome do Integrante 1
- Nome do Integrante 2

## Descrição
Aplicação web que lista livros e permite pesquisar, filtrar e paginar os registros.

### Modelos
- **Autor** (`nome`, `nacionalidade`)
- **Genero** (`nome`)
- **Livro** (`titulo`, `ano_publicacao`, `nota`, `sinopse`, `autor` → FK, `genero` → FK)

### Filtros implementados
| Filtro | Campo | Como funciona |
|---|---|---|
| Pesquisa textual | `q` | `Livro.objects.filter(titulo__icontains=q)` |
| Autor | `<select name="autor">` | `filter(autor_id=...)` |
| Gênero | `<select name="genero">` | `filter(genero_id=...)` |

Todos usam o método **GET**, funcionam individualmente ou combinados e são aplicados **antes** da paginação.

### Paginação
`Paginator` com **5 livros por página**, botões *Anterior/Próxima* e indicação "Página X de Y". Os filtros são preservados nos links porque a view monta uma querystring a partir de `request.GET`, removendo apenas o parâmetro `page`.

### Estrutura
```
catalogo/
├── static/catalogo/css/estilo.css     # estilos da página
└── templates/catalogo/lista_livros.html
```

## Como executar
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations catalogo
python manage.py migrate
python manage.py popular        # carrega 25 livros, 6 autores e 5 gêneros
python manage.py createsuperuser  # opcional, para usar o /admin
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/

## Captura de tela
![Listagem com filtros e paginação](docs/screenshot.png)

> Tire a captura com filtros aplicados e paginação visível e salve em `docs/screenshot.png`.
