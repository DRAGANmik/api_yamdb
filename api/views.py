from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer
#from .permissions import IsAuthorOrReadOnly
from django.db.models import Avg

from .models import Title, Category, Genre
from rest_framework import mixins
from .serializers import (TitleSerializer1, TitleSerializer2,
                          CategorySerializer, GenreSerializer)
from .permissions import IsAdmin
from .filters import TitleFilter

class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]
     
    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        queryset = Review.objects.filter(title=title)
        #return title.reviews
        return queryset






class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer1
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_queryset(self):
        queryset = Title.objects.annotate(rating=Avg('reviews__score'))
        return queryset

    def get_serializer_class(self):
        actions = ['list', 'retrieve']
        if self.action in actions:
            return TitleSerializer2
        return TitleSerializer1


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly]
     
    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        queryset = Comment.objects.filter(review=review)
        #return review.comments
        return queryset


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]
