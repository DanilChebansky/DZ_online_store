from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Record(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(max_length=600, verbose_name='Содержимое')
    image = models.ImageField(upload_to='records/', verbose_name='Изображение(превью)', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'запись'  # Настройка для наименования одного объекта
        verbose_name_plural = 'записей'  # Настройка для наименования набора объектов
        ordering = ('created_at',)
