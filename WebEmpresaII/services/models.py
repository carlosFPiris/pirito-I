from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    subtile = models.CharField(max_length=200, verbose_name='subtitulo')
    content = models.TextField()
    image = models.ImageField(upload_to="services")
    created = models.DateTimeField(
        verbose_name='Fecha creación', auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name='Última modificación', auto_now=True,)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title
