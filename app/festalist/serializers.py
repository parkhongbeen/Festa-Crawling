from rest_framework import serializers
from .models import FestaList


class FestaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FestaList
        fields = (
            'pk',
            'author',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )


# class FestaListCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FestaList
#         fields = (
#             'pk',
#             'author',
#             'title',
#             'code',
#             'linenos',
#             'language',
#             'style',
#         )
#
#         def to_representation(self, instance):
#             return FestaListSerializer(instance).data
