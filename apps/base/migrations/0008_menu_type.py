# Generated by Django 4.2.7 on 2023-11-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(default=1, max_length=255, verbose_name='Тип блюда'),
            preserve_default=False,
        ),
    ]
