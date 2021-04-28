from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .serializers import UserSerializer,\
    DetailSerializer, EmailConfirmationSerializer, TokenSerializer
from .models import User
from .permissions import IsADM
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken


class TokenAPI(APIView):
    serializer_class = TokenSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        confirmation_code = self.request.data.get('confirmation_code')
        try:
            user = get_object_or_404(User, email=email, confirmation_code=confirmation_code)
            token = AccessToken.for_user(user)
            # refresh
            user.confirmation_code = default_token_generator.make_token(user)
            return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EmailConfirmationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = EmailConfirmationSerializer

    def post(self, request):
        user = User.objects.get(email=request.data['email'])
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        send_mail('Confirmation',
                  f'Your code: {confirmation_code}',
                  'admin@admin.ru',
                  [request.data['email']])
        return Response({'status': "send email"}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsADM, permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=['get', 'patch'],
        url_path='me',
        url_name='me',
        permission_classes=[permissions.IsAuthenticated]
    )
    def view_me(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = DetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
