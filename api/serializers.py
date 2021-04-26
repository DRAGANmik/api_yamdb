from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Category, Genre, Title, Review, Comment
from users.models import User
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category

    def to_representation(self, instance):
        category = super().to_representation(instance)

        return {'name': category['name'],
                'slug': category['slug']}


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre

    def to_representation(self, instance):
        category = super().to_representation(instance)

        return {'name': category['name'],
                'slug': category['slug']}


class TitleSerializer1(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field='slug', many=True)
    rating = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer2(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(required=False, read_only=True, many=True)
    rating = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    #title = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review
        #validators=[UniqueValidator(queryset=User.objects.all())]
        # validators = [UniqueTogetherValidator(
        #     queryset=Review.objects.all(),
        #     fields=['author', 'title', ],
        #     message='Вы уже комментировали данное произведение')]
    # def validate(self, data):
    #     if data['user'] == data['following']:
    #         raise serializers.ValidationError(
    #             'Невозможно подписаться на самого себя'
    #         )
    #     return data
    # def validate_title(self, user):
    #     unique_pair = Review.objects.filter(
    #         title=self.data.get('title_id'),
    #         author__username=user
    #     )
    #     if unique_pair.exists():
    #         raise serializers.ValidationError('Подписка уже оформлена')
    #     return user

    def validate(self, data):
        title_id = self.context['request'].parser_context['kwargs'].get('title_id')
        author = self.context['request'].user
        current_title = get_object_or_404(Title,id=title_id)
        if (self.context['request'].method == 'POST'
                and current_title.reviews.filter(author=author).exists()):
            raise serializers.ValidationError('Отзыв на это произведение уже существует')
        return data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment

