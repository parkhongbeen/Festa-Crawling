from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
<<<<<<< HEAD
from rest_framework.pagination import LimitOffsetPagination
=======
from rest_framework.pagination import PageNumberPagination
>>>>>>> d478261c812b082b7f33c6c6a14e09ba063b8a1b
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from festalist.models import FestaList
from festalist.serializers import FestaListSerializer, FestaListKeywordPostSerializer, FestaListKeywordSerializer


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_size = 30


class FestaListAPIView(APIView):
    pagination_class = BasicPagination
    serializer_class = FestaListSerializer

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                                                self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request):
        # def category_pagenation(category):
        #     if category == 'pay':
        #         instance = FestaList.objects.filter(tickets__contains="₩")
        #     elif category == 'free':
        #         instance = FestaList.objects.filter(tickets__contains="무료")
        #     elif category == 'exterior':
        #         instance = FestaList.objects.filter(tickets="")
        #     else:
        #         instance = FestaList.objects.all()
        #
        #     page = self.paginate_queryset(instance)
        #     if page is not None:
        #         serializer = self.get_paginated_response(self.serializer_class(page,
        #                                                                        many=True).data)
        #     else:
        #         serializer = self.serializer_class(instance, many=True)
        #
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        #
        # category = request.query_params.get('category')
        # category_pagenation(category)

        category = request.query_params.get('category')
        if category == 'pay':
            instance = FestaList.objects.filter(tickets__contains="₩")
        elif category == 'free':
            instance = FestaList.objects.filter(tickets__contains="무료")
        elif category == 'exterior':
            instance = FestaList.objects.filter(tickets="")
        else:
            instance = FestaList.objects.all()

        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
                                                                           many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)

<<<<<<< HEAD
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
=======
        return Response(serializer.data, status=status.HTTP_200_OK)
>>>>>>> d478261c812b082b7f33c6c6a14e09ba063b8a1b


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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            user = Token.objects.get(key=request.auth).user
            keyword = user.festalistkeyword_set.get(id=pk)
            user.festalistkeyword_set.remove(keyword)
            return Response(data={'data': '데이터를 삭제하였습니다.'}, status=status.HTTP_200_OK)
        except:
            return Response(data={"detail": "존재하지 않는 사용자입니다."}, status=status.HTTP_204_NO_CONTENT)
