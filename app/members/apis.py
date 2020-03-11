from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from members.serializers import UserSerializer


class CheckUserAPIView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(email=request.GET['email'])
            if user:
                data = {'isExist': True}
                return Response(data, status=status.HTTP_200_OK)
        except:
            data = {"isExist": False}
            return Response(data)


# 사용자로그인 --> 아이디/비번/이메일 전달 --> 유효 검사후 토큰 반환
# 로그인
class AuthTokenAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)

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


# 동시 접속 불가. 웹이나 모바일에서 로그아웃하면 서버에서 삭제
# 로그아웃
class LogoutAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(data={"detail": "로그아웃 하셨습니다."}, status=status.HTTP_200_OK)


# 회원 가입
class CreateUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'user': serializer.data,
                'detail': f'{request.data["email"]}로 새로운 계정을 생성하셨습니다'
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
