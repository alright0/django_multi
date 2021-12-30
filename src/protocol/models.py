from typing import TYPE_CHECKING
from django.db import models

def directory_images(instance, filename):
    return f'protocols/{instance.parent.id}/images/{filename}'

class Protocol(models.Model):
    class Meta:
        verbose_name = "Протокол"
        verbose_name_plural = "Протоколы"

    TYPE_CHOICES =(
        ("test1", "Протокол 1"),
        ("test2", "Протокол 2"),
    )

    type = models.CharField(max_length=140, verbose_name="Тип", choices=TYPE_CHOICES)
    title = models.CharField(max_length=140, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return self.title


class Screen(models.Model):
    class Meta:
        verbose_name = "Экран"
        verbose_name_plural = "Экраны"

    TEXT_SCREEN = 'TextScreen'
    FILE_SCREEN = 'FileScreen'
    IMAGE_SCREEN = 'ImageScreen'
    COMPLEX_SCREEN = 'ComplexScreen'


    TYPE_CHOICES = (
        (TEXT_SCREEN, "Текст"),
        (FILE_SCREEN, "Файл"),
        (IMAGE_SCREEN, "Изображение"),
        (COMPLEX_SCREEN, "Мульти"),
    )

    type = models.CharField(max_length=140, verbose_name="Тип", choices=TYPE_CHOICES, null=True, blank=True)
    title = models.CharField(max_length=140, verbose_name="Название", null=True, blank=True)
    description = models.TextField(default="", verbose_name="Описание", null=True, blank=True)
    parent = models.ForeignKey(
        "protocol.Protocol", on_delete=models.CASCADE, verbose_name="Протокол", null=True, blank=True
    )
    key = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    image = models.ImageField(upload_to=directory_images, null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f"{self.parent} - {self.title}"
  