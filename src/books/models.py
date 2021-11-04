from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    category = models.CharField(max_length=250, verbose_name="Категория")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
