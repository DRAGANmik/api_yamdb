from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MeDetail, RegistationAPIView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path(r'v1/users/me/', MeDetail.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/email/', RegistationAPIView.as_view()),
]
