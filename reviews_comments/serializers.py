from rest_framework import serializers
from .models import  Category, Genre, Title, Review, Comment
from rest_framework.validators import UniqueTogetherValidator


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    title = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        fields =  '__all__'
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
        fields =  '__all__'
        model = Comment
