# Generated by Django 4.2.7 on 2023-11-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_experience_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_all', verbose_name='все блюда')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'все блюда',
                'verbose_name_plural': 'все блюда',
            },
        ),
        migrations.CreateModel(
            name='Desserts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_dessert', verbose_name='десерт')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'десерт',
                'verbose_name_plural': 'десерты',
            },
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_dinner', verbose_name='ужин')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'ужин',
                'verbose_name_plural': 'ужин',
            },
        ),
        migrations.CreateModel(
            name='Restuarant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_restuarant', verbose_name='рестаран')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'наш рестаран',
                'verbose_name_plural': 'наш рестаран',
            },
        ),
    ]