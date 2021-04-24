from rest_framework import serializers
from .models import  Category, Genre, Title, Review, Comment, Title
from rest_framework.validators import UniqueTogetherValidator


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    title = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'
        model = Review
        validators = [UniqueTogetherValidator(
            queryset=Review.objects.all(),
            fields=['author', 'title', ],
            message='Вы уже комментировали данное произведение')]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
