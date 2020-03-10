from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from festalist.models import FestaList
from festalist.serializers import FestaListSerializer, FestaListKeywordPostSerializer, FestaListKeywordSerializer
from members.models import User


class FestaListAPIView(APIView):
    def get(self, request):
        pay = FestaList.objects.filter(tickets__contains="₩")
        free = FestaList.objects.filter(tickets__contains="무료")
        exterior = FestaList.objects.filter(tickets="")

        serializer_pay = FestaListSerializer(pay, many=True)
        serializer_free = FestaListSerializer(free, many=True)
        serializer_exterior = FestaListSerializer(exterior, many=True)
        data = {
            'pay': serializer_pay.data,
            'free': serializer_free.data,
            'outerEvent': serializer_exterior.data
        }
        return Response(data)


class FestaListDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            festalist = FestaList.objects.get(pk=pk)
            serializer = FestaListSerializer(festalist)
            data = {
                'listDetail': serializer.data
            }
            return Response(data)
        except:
            return Response(data={"detail": "잘못된 이벤트 입니다"}, status=status.HTTP_204_NO_CONTENT)


class FestaListKeywordUpload(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            keywords = user.festalistkeyword_set.all()
            serializer = FestaListKeywordSerializer(keywords, many=True)
            data = {
                'keywords': serializer.data
            }
            return Response(data)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        try:
            serializer = FestaListKeywordPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(pk)
                data = {
                    'data': serializer.data
                }
                return Response(data)
            else:
                return Response(serializer.errors)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)
