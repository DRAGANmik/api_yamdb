from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Category, Genre, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category

class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(required=False, read_only=True, many=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                         slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                          slug_field='slug')
    class Meta:
        fields = '__all__'
        model = Title

    



    


