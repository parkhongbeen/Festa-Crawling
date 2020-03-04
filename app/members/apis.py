from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers import UserSerializer


# 사용자로그인 --> 아이디/비번/이메일 전달 --> 유효 검사후 토큰 반환
class AuthTokenAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        # email = request.data['email']

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
        else:
            raise AuthenticationFailed()

        serializer = UserSerializer(user)
        data = {
            'token': token.key,
            'user': serializer.data
        }
        return Response(data)

    def get(self, request):
        print('리퀘스트 유저는 : ', request.user)
        print('리퀘스트 어스는 : ', request.auth)
        data = {
            'user': request.user,
            'auth': request.auth
        }
        return Response(data)


class CreateUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'user': serializer.data
            }
            return Response(data)

        else:
            return Response(serializer.errors)