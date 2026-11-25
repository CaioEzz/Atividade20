from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Autor, Genero, Livro

AUTORES = [
    ("Machado de Assis", "Brasileiro"),
    ("Clarice Lispector", "Brasileira"),
    ("George Orwell", "Britânico"),
    ("J. R. R. Tolkien", "Britânico"),
    ("Agatha Christie", "Britânica"),
    ("Isaac Asimov", "Russo-americano"),
]

GENEROS = ["Romance", "Contos", "Fantasia", "Ficção Científica", "Mistério"]

# (título, ano, nota, autor, gênero, sinopse)
LIVROS = [
    ("Dom Casmurro", 1899, "9.3", "Machado de Assis", "Romance", "Bentinho narra sua vida e a dúvida sobre Capitu."),
    ("Memórias Póstumas de Brás Cubas", 1881, "9.5", "Machado de Assis", "Romance", "Um defunto autor conta sua vida com ironia."),
    ("Quincas Borba", 1891, "8.8", "Machado de Assis", "Romance", "Rubião herda uma fortuna e a filosofia do Humanitismo."),
    ("Esaú e Jacó", 1904, "8.5", "Machado de Assis", "Romance", "Irmãos gêmeos rivais em meio à queda do Império."),
    ("Helena", 1876, "8.0", "Machado de Assis", "Romance", "Uma jovem é reconhecida como filha de um conselheiro."),
    ("A Hora da Estrela", 1977, "9.0", "Clarice Lispector", "Romance", "A vida simples da nordestina Macabéa no Rio de Janeiro."),
    ("Perto do Coração Selvagem", 1943, "8.7", "Clarice Lispector", "Romance", "O fluxo de consciência de Joana, da infância à vida adulta."),
    ("A Paixão Segundo G.H.", 1964, "8.9", "Clarice Lispector", "Romance", "Uma mulher tem um encontro transformador com uma barata."),
    ("Laços de Família", 1960, "8.8", "Clarice Lispector", "Contos", "Treze contos sobre relações cotidianas e epifanias."),
    ("1984", 1949, "9.6", "George Orwell", "Ficção Científica", "Winston vive sob o olhar do Grande Irmão."),
    ("A Revolução dos Bichos", 1945, "9.2", "George Orwell", "Romance", "Animais tomam a fazenda e reproduzem a tirania."),
    ("Dias na Birmânia", 1934, "7.6", "George Orwell", "Romance", "Um oficial colonial enfrenta os dilemas do império."),
    ("Na Pior em Paris e em Londres", 1933, "7.9", "George Orwell", "Romance", "Relato da pobreza vivida nas duas capitais."),
    ("O Hobbit", 1937, "9.4", "J. R. R. Tolkien", "Fantasia", "Bilbo parte numa aventura com treze anões."),
    ("A Sociedade do Anel", 1954, "9.5", "J. R. R. Tolkien", "Fantasia", "Frodo inicia a jornada para destruir o Um Anel."),
    ("As Duas Torres", 1954, "9.3", "J. R. R. Tolkien", "Fantasia", "A Sociedade se divide e a guerra se aproxima."),
    ("O Retorno do Rei", 1955, "9.5", "J. R. R. Tolkien", "Fantasia", "A batalha final pela Terra-média."),
    ("Assassinato no Expresso do Oriente", 1934, "9.1", "Agatha Christie", "Mistério", "Poirot investiga um crime em um trem bloqueado pela neve."),
    ("O Assassinato de Roger Ackroyd", 1926, "9.2", "Agatha Christie", "Mistério", "Um dos finais mais famosos da literatura policial."),
    ("E Não Sobrou Nenhum", 1939, "9.4", "Agatha Christie", "Mistério", "Dez convidados presos em uma ilha e mortos um a um."),
    ("Morte no Nilo", 1937, "8.9", "Agatha Christie", "Mistério", "Crime a bordo de um cruzeiro pelo Egito."),
    ("Eu, Robô", 1950, "9.0", "Isaac Asimov", "Ficção Científica", "Contos sobre as Três Leis da Robótica."),
    ("Fundação", 1951, "9.3", "Isaac Asimov", "Ficção Científica", "A psico-história tenta salvar o futuro da galáxia."),
    ("O Fim da Eternidade", 1955, "8.7", "Isaac Asimov", "Ficção Científica", "Uma organização manipula a história através do tempo."),
    ("Os Próprios Deuses", 1972, "8.6", "Isaac Asimov", "Ficção Científica", "Troca de matéria com um universo paralelo."),
]


class Command(BaseCommand):
    help = "Popula o banco com autores, gêneros e livros de exemplo."

    def handle(self, *args, **options):
        autores = {}
        for nome, nacionalidade in AUTORES:
            autores[nome], _ = Autor.objects.get_or_create(
                nome=nome, defaults={"nacionalidade": nacionalidade}
            )

        generos = {}
        for nome in GENEROS:
            generos[nome], _ = Genero.objects.get_or_create(nome=nome)

        criados = 0
        for titulo, ano, nota, autor, genero, sinopse in LIVROS:
            _, created = Livro.objects.get_or_create(
                titulo=titulo,
                defaults={
                    "ano_publicacao": ano,
                    "nota": Decimal(nota),
                    "sinopse": sinopse,
                    "autor": autores[autor],
                    "genero": generos[genero],
                },
            )
            criados += created

        self.stdout.write(
            self.style.SUCCESS(f"{criados} livros criados (total: {Livro.objects.count()}).")
        )
