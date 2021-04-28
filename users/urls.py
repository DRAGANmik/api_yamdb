from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EmailConfirmationAPIView, TokenAPI

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/email/', EmailConfirmationAPIView.as_view()),
    path('v1/auth/token/', TokenAPI.as_view())
]
