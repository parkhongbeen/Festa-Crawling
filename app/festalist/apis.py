from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
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

        # pagination_class = LimitOffsetPagination
        # page_number = self.request.query_params.get('page_number ', 1)
        # page_size = self.request.query_params.get('page_size ', 30)
        # paginator = Paginator(news, page_size)
        # serializer = FestaListSerializer(paginator.page(page_number), many=True, context={'request': request})
        # response = Response(serializer.data, status=status.HTTP_200_OK)
        # return response

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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            user = Token.objects.get(key=request.auth).user
            keywords = user.festalistkeyword_set.all()
            serializer = FestaListKeywordSerializer(keywords, many=True)
            data = {
                'keywords': serializer.data
            }
            return Response(data)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        try:
            user = Token.objects.get(key=request.auth).user
            serializer = FestaListKeywordPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user.id)
                data = {
                    'data': serializer.data
                }
                return Response(data)
            else:
                return Response(serializer.errors)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)


class FestaListKeywordDelete(APIView):
    """
    여러가지 키워드가 있을건데, 키워드를 클릭하면 해당 키워드를 삭제.
    """

    def delete(self, request, pk):
        try:
            user = Token.objects.get(key=request.auth).user
            keyword = user.festalistkeyword_set.get(id=pk)
            user.festalistkeyword_set.remove(keyword)
            return Response(data={'data': '데이터를 삭제하였습니다.'},status=status.HTTP_200_OK)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)

