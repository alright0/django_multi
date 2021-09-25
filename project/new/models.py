from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Название"
    )
    author = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
