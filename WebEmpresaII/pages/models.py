from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    order = models.SmallIntegerField(default=0)
    content = RichTextField(verbose_name='Contenido')

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "Páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
