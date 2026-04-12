from django.db import models


class Pr(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание товара', help_text='Введите описание товара')
    photo = models.ImageField(upload_to='templates/photo', verbose_name='Фото', help_text='Загрузите фото товара')
    category = models.CharField(max_length=150, verbose_name='Категория', help_text='Введите категорию')
    price = models.FloatField(verbose_name='Цена за покупку', help_text='Введите цену')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True )
    updated_at = models.DateTimeField(verbose_name='Дата создания', auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price',]

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]