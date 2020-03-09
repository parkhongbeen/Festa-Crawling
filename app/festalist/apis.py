from rest_framework.response import Response
from rest_framework.views import APIView
from festalist.models import FestaList
from festalist.serializers import FestaListSerializer


class FestaListAPIView(APIView):
    def get(self, request):
        pay = FestaList.objects.filter(tickets__contains="₩")
        free = FestaList.objects.filter(tickets__contains="무료")
        exterior = FestaList.objects.filter(tickets="")

        serializer_pay = FestaListSerializer(pay, many=True)
        serializer_free = FestaListSerializer(free, many=True)
        serializer_exterior = FestaListSerializer(exterior, many=True)
        data = {
            '유료': serializer_pay.data,
            '무료': serializer_free.data,
            '외부이벤트': serializer_exterior.data
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
