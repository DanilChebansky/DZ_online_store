from django.core.exceptions import ValidationError
from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=600, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)
    user_owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} - {self.price} руб. за шт.'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product} - версия {self.version_number} ({self.version_name})'

    class Meta:
        verbose_name = 'версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'версии'  # Настройка для наименования набора объектов
        ordering = ('version_number',)

    def clean(self):
        if self.is_active and Version.objects.filter(
                product=self.product, is_active=True
        ).exclude(pk=self.pk).exists():
            raise ValidationError(
                'У этого продукта уже есть активная версия.'
            )

    def save(self, *args, **kwargs):
        self.clean()  # вызываем clean перед сохранением
        super().save(*args, **kwargs)
