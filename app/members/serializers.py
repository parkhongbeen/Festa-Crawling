from rest_framework import serializers

from members.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def save(self, **kwargs):
        password = self.validated_data['password']
        email = self.validated_data['email']
        user = User.objects.create_user(
            password=password,
            email=email
        )
        return user


class UsernameCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

