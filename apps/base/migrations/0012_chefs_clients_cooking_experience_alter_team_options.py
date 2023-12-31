# Generated by Django 4.2.7 on 2023-11-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=255, verbose_name='Опытные повара')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Опытные повара',
                'verbose_name_plural': 'Опытные повара',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happy_clients', models.CharField(max_length=255, verbose_name='Счастливые клиенты')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Счастливые клиенты',
                'verbose_name_plural': 'Счастливые клиенты',
            },
        ),
        migrations.CreateModel(
            name='Cooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255, verbose_name='время приготовлении')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'время приготовлении',
                'verbose_name_plural': 'время приготовлении',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='год')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'счястливые клиенты',
                'verbose_name_plural': 'счястливые клиенты',
            },
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': ('Команда',), 'verbose_name_plural': 'Команда'},
        ),
    ]
