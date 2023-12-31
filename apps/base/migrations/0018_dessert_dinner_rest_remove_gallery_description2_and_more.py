# Generated by Django 4.2.7 on 2023-11-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_gallery_description2_gallery_description3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_dessert', verbose_name='дессерт')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'дессерт',
                'verbose_name_plural': 'дессерты',
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
            name='Rest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_rest', verbose_name='рессторан')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('name', models.CharField(max_length=255, verbose_name='название блюды')),
            ],
            options={
                'verbose_name': 'рессторан',
                'verbose_name_plural': 'рессторан',
            },
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='name3',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='name4',
        ),
    ]
