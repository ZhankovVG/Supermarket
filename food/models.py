from django.db import models
from django.urls import reverse



class Category(models.Model):
    # Категории
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug' : self.url})


class Manufacturer(models.Model):
    # Производитель
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='manufacturer/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def get_absolute_url(self):
        return reverse('country', kwargs={'slug' : self.name})


class Product(models.Model):
    # Продукты
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    weight = models.FloatField('Вес', blank=True, default=0)
    photo = models.ImageField('Изображение', upload_to='Products/')
    draft = models.BooleanField('В наличии', default=False)
    url = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    manufacturer = models.ManyToManyField(Manufacturer, verbose_name='Производитель')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('datail', kwargs={'slug' : self.url})


class RatingsStar(models.Model):
    # Звезда рейтинга
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'
    
    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    # Рейтинг
    ip = models.CharField('IP адресс', max_length=50)
    star = models.ForeignKey(RatingsStar, on_delete=models.CASCADE, verbose_name='Звезда')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return self.star
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Comments(models.Model):
    # Коментарий
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Коментфрий', max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Родитель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукты')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'