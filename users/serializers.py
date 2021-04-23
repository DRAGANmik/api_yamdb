from rest_framework import serializers
from .models import User
from django.core.mail import send_mail


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']

    def create(self, validated_data):
        email = validated_data['email']
        username = email.split('@')[:1]
        username = ''.join(map(str, username))
        password = User.objects.make_random_password()

        user = User(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()

        send_mail(
            'Быстрая регистрация',
            f'Спасибо за регистрацию {username}, вот ваш временный пароль {password}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'bio', 'role']


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'bio', 'role']
        read_only_fields = ('role',)

