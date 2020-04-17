from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category (models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(
        verbose_name='Fecha creación', auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='Última modificación', auto_now=True,)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Autor")
    published = models.DateTimeField(
        default=now, verbose_name="Fecha de publicación")
    categories = models.ManyToManyField(
        Category, verbose_name="Categorias", related_name="get_post")
    image = models.ImageField(verbose_name="Imagen",
                              upload_to="blog", null=True, blank=True)
    created = models.DateTimeField(
        verbose_name='Fecha creación', auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='Última modificación', auto_now=True,)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title
