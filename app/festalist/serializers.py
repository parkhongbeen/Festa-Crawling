from rest_framework import serializers

from .models import FestaList


class FestaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaList
        fields = ['title', 'host', 'date', 'content', 'apply', 'tickets', 'link', 'image']
