from rest_framework.response import Response
from rest_framework.views import APIView

from festalist.models import FestaList
from festalist.serializers import FestaListSerializer


class FestaListAPIView(APIView):
    def get(self, request):
        festalist = FestaList.objects.all()
        serializer = FestaListSerializer(festalist, many=True)
        data = {
            'list': serializer.data
        }
        return Response(data)


class FestaListDetailAPIView(APIView):
    def get(self, request, pk):
        festalist = FestaList.objects.get(pk=pk)
        serializer = FestaListSerializer(festalist)
        data = {
            'listDetail': serializer.data
        }
        return Response(data)
