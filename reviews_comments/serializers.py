from rest_framework import serializers
from .models import Comment, Review 
from django.contrib.auth import get_user_model

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        fields =  '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields =  '__all__'
        model = Comment