from rest_framework import serializers

from .models import Category, Genre, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category

    def to_representation(self, instance):
        category = super().to_representation(instance)

        return {'name': category['name'],
                'slug': category['slug']}


class TitleSerializer1(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         slug_field='slug', many=True)

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializer2(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    genre = GenreSerializer(required=False, read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Title
