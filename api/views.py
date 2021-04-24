from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Comment, Review, Title
from django.contrib.auth.models import User
from .serializers import CommentSerializer, ReviewSerializer, TitleSerializer
from .permissions import IsAuthorOrReadOnly
from django.db.models import Avg


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer

    def get_queryset(self):
        queryset = Title.objects.annotate(rating=Avg('reviews__score'))
        return queryset



class ReviewViewSet(viewsets.ModelViewSet):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
     
    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        queryset = Review.objects.filter(title=title)
        #return title.reviews
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
     
    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        queryset = Comment.objects.filter(review=review)
        #return review.comments
        return queryset
