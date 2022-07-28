from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.models import Account
from apps.account.serializers import (
    AccountDeleteSerializer,
    AccountDetailSerializer,
    SignInSerializer,
    SignUpSerializer,
)
from apps.utils import IsOwnerOrReadOnly


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
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# api/v1/accounts/<int:pk>
class AccountView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Account.objects.filter(is_active=True, pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountDetailSerializer
        elif self.request.method == "PUT":
            return AccountDetailSerializer
        elif self.request.method == "DELETE":
            return AccountDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
