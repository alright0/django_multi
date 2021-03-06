# Generated by Django 3.2.6 on 2021-12-27 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0005_auto_20211227_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protocol.protocol', verbose_name='Протокол'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='title',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='type',
            field=models.CharField(blank=True, choices=[('TextScreen', 'Текст'), ('FileScreen', 'Файл'), ('ImageScreen', 'Изображение'), ('ComplexScreen', 'Мульти')], max_length=140, null=True, verbose_name='Тип'),
        ),
    ]
