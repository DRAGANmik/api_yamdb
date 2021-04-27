from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Category, Genre, Title, Review, Comment


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


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field='slug', many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(required=False, read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review

    def validate(self, data):
        title_id = (self.context['request'].
                    parser_context['kwargs'].get('title_id'))
        author = self.context['request'].user
        current_title = get_object_or_404(Title, id=title_id)
        if (self.context['request'].method == 'POST'
                and current_title.reviews.filter(author=author).exists()):
            raise serializers.ValidationError(
                'Отзыв на это произведение уже существует'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment
