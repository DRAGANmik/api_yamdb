from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import serializers

from users.models import User


class TokenSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    confirmation_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'confirmation_code']

    def validate(self, data):
        email = data['email']
        confirmation_code = data['confirmation_code']
        user = User.objects.filter(
            email=email,
            confirmation_code=confirmation_code
        )
        if not user.exists():
            raise serializers.ValidationError(
                'Неверный email или confirmation_code'
            )
        return data


class EmailConfirmationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ['email']

    def create(self, validated_data):
        email = validated_data['email']

        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': email}
        )

        if created:
            password = User.objects.make_random_password()
            user.set_password(password)

        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        send_mail('Confirmation_code',
                  f'Your code: {confirmation_code}',
                  'admin@admin.ru',
                  [email])
        return user


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


class DetailSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)
