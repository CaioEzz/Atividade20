from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    nacionalidade = models.CharField(max_length=60, blank=True)

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "gênero"
        verbose_name_plural = "gêneros"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("título", max_length=150)
    ano_publicacao = models.PositiveIntegerField("ano de publicação")
    nota = models.DecimalField(max_digits=3, decimal_places=1, help_text="Nota de 0 a 10")
    sinopse = models.TextField(blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros")
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name="livros")

    class Meta:
        verbose_name = "livro"
        verbose_name_plural = "livros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
