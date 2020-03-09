from rest_framework.response import Response
from rest_framework.views import APIView

from festalist.models import FestaList, FestaListKeyword
from festalist.serializers import FestaListSerializer, FestaListKeywordSerializer, FestaListKeywordPostSerializer


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


class FestaListKeywordUpload(APIView):
    def get(self, request, pk):
        keywords = FestaListKeyword.objects.filter(event_id=pk)
        serializer = FestaListKeywordSerializer(keywords, many=True)
        data = {
            'keywords': serializer.data
        }
        return Response(data)

    def post(self, request, pk):
        serializer = FestaListKeywordPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pk)
            data = {
                'data': serializer.data
            }
            return Response(data)
        else:
            return Response(serializer.errors)
