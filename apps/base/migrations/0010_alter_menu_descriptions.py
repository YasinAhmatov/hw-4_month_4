# Generated by Django 4.2.7 on 2023-11-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_menu_сlever_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descriptions',
            field=models.TextField(max_length=255, verbose_name='Описание блюда'),
        ),
    ]
