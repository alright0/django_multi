from typing import TYPE_CHECKING
from django.db import models


class Protocol(models.Model):
    class Meta:
        verbose_name = "Протокол"
        verbose_name_plural = "Протоколы"

    TYPE_CHOICES = (
        ("TypeOne", "Тип 1"),
        ("TypeOne", "Тип 2"),
        ("TypeOne", "Тип 3"),
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

    TYPE_CHOICES = (
        ("TextScreen", "Текст"),
        ("FileScreen", "Файл"),
        ("ImageScreen", "Изображение"),
        ("ComplexScreen", "Мульти"),
    )

    type = models.CharField(max_length=140, verbose_name="Тип", choices=TYPE_CHOICES)
    title = models.CharField(max_length=140, verbose_name="Название")
    description = models.TextField(default="", verbose_name="Описание")
    parent = models.ForeignKey(
        "protocol.Protocol", on_delete=models.CASCADE, verbose_name="Протокол"
    )
    key = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.parent} - {self.title}"
