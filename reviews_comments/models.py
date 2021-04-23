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


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                             max_length=200)
    slug = models.SlugField(verbose_name="Адрес для жанра",
                            max_length=100,
                            unique=True,
                            help_text='Используйте латиницу')
    

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField()
    year = models.DateTimeField(
        "Год публикации", auto_now_add=True)
    
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
    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    title= models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name="reviews"
    )
    pub_date = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    pub_date = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.text


class Rating(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name="rating"
    )
    score = models.ForeignKey(
        
    )
