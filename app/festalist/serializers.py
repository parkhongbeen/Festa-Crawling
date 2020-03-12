from rest_framework import serializers

from members.models import User
from .models import FestaList, FestaListKeyword


class FestaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaList
        fields = ['id', 'title', 'host', 'date', 'content', 'apply', 'tickets', 'link', 'image']


class FestaListKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaListKeyword
        fields = ['id', 'keyword']


class FestaListKeywordPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaListKeyword
        fields = ['id', 'keyword']

    def save(self, *args):
        keyword = self.validated_data['keyword']
        user = User.objects.get(id=int(args[0]))
        # get_or_create 는 튜플을 돌려준다
        val = FestaListKeyword.objects.get_or_create(
            keyword=keyword
        )[0]
        val.user.add(user)


class FestaListKeywordDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaListKeyword
        fields = ['id', 'keyword']