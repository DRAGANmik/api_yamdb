from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Category, Genre, Title
from django.contrib.auth import get_user_model
User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category

class TitleSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(required=False, read_only=True, many=True)
    genre = GenreSerializer(required=False, read_only=True, many=True)     
    class Meta:
        fields = ('id', 'name','genre', 'category', 'year' )
        model = Title





    


