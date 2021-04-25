from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=200)

    slug = models.SlugField(verbose_name="Адрес для категории",
                            max_length=100,
                            unique=True,
                            help_text='Используйте латиницу')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                            max_length=200)
    slug = models.SlugField(verbose_name="Адрес для жанра",
                            max_length=100,
                            unique=True,
                            help_text='Используйте латиницу')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Title(models.Model):
    name = models.TextField(verbose_name='Название')
    year = models.IntegerField()
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 help_text='Выберите категорию',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 blank=True,
                                 null=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр',
                                   help_text='Выберите жанр',
                                   related_name='titles',
                                   blank=True,
                                   null=True)
    description = models.TextField(verbose_name='Описание',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
