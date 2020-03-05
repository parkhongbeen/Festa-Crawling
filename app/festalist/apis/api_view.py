from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import FestaList
from ..serializers import FestaListSerializer


class SnippetListCreateAPIView(APIView):
    def get(self, request):
        festalists = FestaList.objects.all()
        serializer = FestaListSerializer(festalists, many=True)
        return Response(serializer.data)


class SnippetRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(FestaList, pk=pk)

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = FestaListSerializer(snippet)
        return Response(serializer.data)
