from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ReviewViewSet
from .views import TitleViewSet, CategoryViewSet, GenreViewSet

router = DefaultRouter()
router.register('titles', TitleViewSet, basename='Titles')
router.register('categories', CategoryViewSet, basename='Categories')
router.register('genres', GenreViewSet, basename='Genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
]
