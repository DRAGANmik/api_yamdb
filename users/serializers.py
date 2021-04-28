from rest_framework import serializers
from .models import User


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'confirmation_code']


class EmailConfirmationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
            'bio',
            'role'
        ]


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
            'bio',
            'role'
        ]
        read_only_fields = ('role',)
