from rest_framework import serializers
from rest_framework.authtoken.models import Token

from members.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']
