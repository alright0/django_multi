# Generated by Django 3.2.6 on 2021-12-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='title',
            field=models.CharField(max_length=140, verbose_name='Название'),
        ),
    ]