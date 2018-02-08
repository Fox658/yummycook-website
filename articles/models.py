from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # add in thumbnail later
    # add in author later

    # Esta funcion sirve para crear una etiqueta de la tabla article con el nombre de la instancia
    # para que se pueda distinguir entre instancias cuando se llame Article.objects.all()
    # aparecera <QuerySet [<Article: Nombre de articulo>, <Article: Otro nombre de articulo>]> en ves de
    # <QuerySet [<Article: Article object(2)>]>
    # Buscar mas informacion en https://es.wikipedia.org/wiki/Mapeo_objeto-relacional sobre ORM
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:55]+'...'