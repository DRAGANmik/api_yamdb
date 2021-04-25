from rest_framework import serializers
from .models import  Category, Genre, Title, Review, Comment, Title
from rest_framework.validators import UniqueTogetherValidator


from .models import Category, Genre, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre

class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        fields = ['name', 'slug']
        model = Category

    def to_representation(self, instance):
        category = super().to_representation(instance)

        return {'name': category['name'],
                'slug': category['slug']}

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

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
    class Meta:
        fields = '__all__'
        model = Title
