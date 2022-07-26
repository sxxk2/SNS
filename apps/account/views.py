from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.serializers import SignInSerializer, SignUpSerializer


# api/v1/accounts/signup
class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입에 성공했습니다."},
                status=status.HTTP_201_CREATED,
            )
        return Response({"message": "회원가입에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)


# api/v1/accounts/signin
class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(token, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
