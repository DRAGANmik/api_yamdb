from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from users.serializers import UserSerializer,\
    DetailSerializer, EmailConfirmationSerializer, TokenSerializer
from users.models import User
from users.permissions import IsADM
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import AccessToken


class TokenAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(**serializer.validated_data)
        token = AccessToken.for_user(user)
        # refresh
        user.confirmation_code = default_token_generator.make_token(user)
        return Response(
            {'token': str(token)},
            status=status.HTTP_201_CREATED
        )


class EmailConfirmationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = EmailConfirmationSerializer

    def post(self, request):
        serializer = EmailConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'status': "send email"},
            status=status.HTTP_201_CREATED
        )


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsADM, permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        url_path='me',
        url_name='me',
        permission_classes=[permissions.IsAuthenticated]
    )
    def view_me(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = DetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if request.method == "PATCH":
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
