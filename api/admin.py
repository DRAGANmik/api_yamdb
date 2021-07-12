from django.contrib import admin
from django.contrib.admin import register
from api.models import Category, Genre, Title, Comment, Review


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@register(Title)
class TitleAdmin(admin.ModelAdmin):
    pass


@register(Comment)
class Comment(admin.ModelAdmin):
    pass


@register(Review)
class Review(admin.ModelAdmin):
    pass
