
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import Http404
from .serializers import UserSerializer, DetailSerializer, RegistrationSerializer
from .models import User
from .permissions import *


class RegistationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsADM, permissions.IsAuthenticated]


class MeDetail(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, request):
        try:
            return User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        me = self.get_object(request)
        serializer = DetailSerializer(me)
        return Response(serializer.data)

    def patch(self, request):
        me = self.get_object(request)
        serializer = DetailSerializer(me, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

