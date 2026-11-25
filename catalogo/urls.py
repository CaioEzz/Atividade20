from django.urls import path

from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.lista_livros, name="lista_livros"),
]
