from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo_image",
        verbose_name="Логотоип сайта"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телейонный номер"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram",
        blank=True,null = True
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube",
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Основные параметры",
        verbose_name_plural = "Основные параметры"
        
class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография для слайда"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название для слайда"
    )
    descriptions = models.TextField(
        verbose_name="Описание для слайда"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайд",
        verbose_name_plural = "Слайды"
        
class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Описание о нас"
    )
    
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = "О нас",
        verbose_name_plural = "О нас"

class History(models.Model):
    image_1 = models.ImageField(
        upload_to="history_image_1",
        verbose_name = "Первая фотография"
    )
    image_2 = models.ImageField(
        upload_to="history_image_2",
        verbose_name = "Второя фотография"
    )
    descriptions = models.TextField(
        verbose_name="Описание истории"
    )
    
    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = "Наша история",
        verbose_name_plural = "Наша история"
        
class Offer(models.Model):
    image = models.ImageField(
        upload_to="offer_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    descriptions = models.TextField(
        verbose_name="Описание блюда"
    )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип блюда"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Предложение",
        verbose_name_plural = "Предложение"

class Menu(models.Model):
    image = models.ImageField(
        upload_to="image_dish",
        verbose_name='фото еды'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    descriptions = models.TextField(
        max_length=255,
        verbose_name="Описание блюда"
    )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип блюда"
    )
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Меню",
        verbose_name_plural = "Меню"

class Team(models.Model):
    image = models.ImageField(
        upload_to="image_cook",
        verbose_name='фото повара'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='имя повара'
    )
    rank = models.CharField(
        max_length=255,
        verbose_name='звание повара'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='слова повара'
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank=True,null=True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram",
        blank=True,null = True
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube",
        blank=True,null=True
    )
    def __str__(self):
        return self.image
    
    class Meta:
        verbose_name = "Команда",
        verbose_name_plural = "Команда"


class Experience(models.Model):
    year = models.CharField(
        max_length=255,
        verbose_name='год'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='описание'
    )
    def __str__(self):
        return self.year
    
    class Meta:
        verbose_name = "опыт"
        verbose_name_plural = "опыт"

class Cooking(models.Model):
    time = models.CharField(
        max_length=255,
        verbose_name="время приготовлении"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="описание"
    )
    def __str__(self):
        return self.time
    
    class Meta:
        verbose_name = "время приготовлении"
        verbose_name_plural = "время приготовлении"

class Clients(models.Model):
    happy_clients = models.CharField(
        max_length=255,
        verbose_name="Счастливые клиенты"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="описание"
    )
    def __str__(self):
        return self.happy_clients
    
    class Meta:
        verbose_name = "Счастливые клиенты"
        verbose_name_plural = "Счастливые клиенты"

class Chefs(models.Model):
    experience = models.CharField(
        max_length=255,
        verbose_name="Опытные повара"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="описание"
    )
    def __str__(self):
        return self.experience
    
    class Meta:
        verbose_name = "Опытные повара"
        verbose_name_plural = "Опытные повара"

class Gallery(models.Model):
    image = models.ImageField(
        upload_to="image_gallery",
        verbose_name="все блюда"
    )
    description =models.CharField(
        max_length=255,
        verbose_name="описание"
    ) 
    name = models.CharField(
        max_length=255,
        verbose_name="название блюды"
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "все блюда"
        verbose_name_plural = "все блюда"
    
class Dessert(models.Model):
    image = models.ImageField(
        upload_to="image_dessert",
        verbose_name="дессерт"
    )
    description =models.CharField(
        max_length=255,
        verbose_name="описание"
    ) 
    name = models.CharField(
        max_length=255,
        verbose_name="название блюды"
    )
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "дессерт"
        verbose_name_plural = "дессерты"


class Rest(models.Model):
    image = models.ImageField(
        upload_to="image_rest",
        verbose_name="рессторан"
    )
    description =models.CharField(
        max_length=255,
        verbose_name="описание"
    ) 
    name = models.CharField(
        max_length=255,
        verbose_name="название блюды"
    )
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "рессторан"
        verbose_name_plural = "рессторан"


class Dinner(models.Model):
    image = models.ImageField(
        upload_to="image_dinner",
        verbose_name="ужин"
    )
    description =models.CharField(
        max_length=255,
        verbose_name="описание"
    ) 
    name = models.CharField(
        max_length=255,
        verbose_name="название блюды"
    )
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "ужин"
        verbose_name_plural = "ужин"