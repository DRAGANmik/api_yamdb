from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> master
>>>>>>> 06ffc1ee8fc2610ef55325a80006d4807a7158c6
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

<<<<<<< HEAD
=======

>>>>>>> 06ffc1ee8fc2610ef55325a80006d4807a7158c6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'api/v1/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path(
        'api/v1/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
<<<<<<< HEAD
    path('api/', include('users.urls')),
=======
    path('api/', include('api.urls'))
>>>>>>> 06ffc1ee8fc2610ef55325a80006d4807a7158c6
]
