from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer, UserChangeSerializer, UserFindSerializer, UserDeleteSerializer, UserListSerializer, MyTokenObtainPairSerializer


# 로그인
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# 로그아웃


class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
# 회원가입


class SignUp(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': '회원가입 성공'}, status=status.HTTP_201_CREATED)
        return Response(data={'message': serializer.error_messages + '회원가입 실패'}, status=status.HTTP_400_BAD_REQUEST)
# 회원정보 수정


class Update(APIView):
    def put(self, request, format=None):
        serializer = UserDetailSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': '회원정보 수정 성공'}, status=status.HTTP_200_OK)
        return Response(data={'message': '회원정보 수정 실패'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(
            request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 회원상세정보
class Detail(APIView):
    def get(self, request, format=None):
        serializer = UserDetailSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
# 회원탈퇴


class Delete(APIView):
    def delete(self, request, format=None):
        serializer = UserDeleteSerializer(request.user)
        request.user.delete()
        return Response(data={'message': '회원탈퇴 성공'}, status=status.HTTP_200_OK)
# 비밀번호 찾기


class FindPassword(APIView):
    def get(self, request, format=None):
        serializer = UserFindSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
# 비밀번호 변경


class ChangePassword(APIView):
    def patch(self, request, format=None):
        serializer = UserChangeSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': '비밀번호 변경 성공'}, status=status.HTTP_200_OK)
        return Response(data={'message': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
# 회원목록


class List(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
