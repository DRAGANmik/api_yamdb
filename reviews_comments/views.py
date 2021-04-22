from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Comment, Review
from django.contrib.auth.models import User
from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsAuthorOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]