import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.account.models import Account
from apps.account.permissions import IsOwnerOrReadOnly
from apps.account.serializers import (
    AccountDeleteSerializer,
    AccountDetailSerializer,
    SignInSerializer,
    SignUpSerializer,
)
from apps.account.swagger import (
    AccountDeleteResponse,
    AccountRestoreResponse,
    AccountRestoreSchema,
    KakaoSignInResponse,
    SignInResponse,
    SignUpResponse,
)


# api/v1/accounts/signup
class SignUpView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SignUpSerializer, responses=SignUpResponse)
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입에 성공했습니다."},
                status=status.HTTP_201_CREATED,
            )
        return Response({"message": "회원가입에 실패했습니다."}, status=400)


# api/v1/accounts/signin
class SignInView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SignInSerializer, responses=SignInResponse)
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
class AccountView(RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    allowed_methods = ["GET", "PATCH", "DELETE"]

    def get_queryset(self):
        queryset = Account.objects.filter(is_active=True, pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountDetailSerializer
        elif self.request.method == "PATCH":
            return AccountDetailSerializer
        elif self.request.method == "DELETE":
            return AccountDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    inherited from RetrieveUpdateAPIView
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    """

    @swagger_auto_schema(responses=AccountDeleteResponse)
    def delete(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# api/v1/accounts/restore
class AccountRestoreView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=AccountRestoreSchema, responses=AccountRestoreResponse)
    def patch(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if Account.objects.filter(email=email).exists():
            account = Account.objects.get(email=email)

            if account.is_active:
                raise exceptions.ValidationError("잘못된 접근입니다.")  # 삭제되지 않은 계정

            if not account.check_password(password):
                raise exceptions.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")
        else:
            raise exceptions.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")

        account.is_active = True
        account.deleted_at = None
        account.save()
        return Response({"message": "계정이 복구되었습니다."}, status=status.HTTP_200_OK)


# api/v1/accounts/kakao/signin
class KakaoSignInView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(responses=KakaoSignInResponse)
    def post(self, reqeust):
        try:
            access_token = reqeust.data["access_token"]  # 카카오에서 전달받은 엑세스토큰
            account_info = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}
            ).json()
            email = account_info["kakao_account"]["email"]

            if Account.objects.filter(email=email).exists():
                account = Account.objects.get(email=email)
            else:
                account = Account.objects.create(email=email)

            # 서비스의 토큰 발급
            token = TokenObtainPairSerializer.get_token(account)
            access_token = str(token.access_token)
            refresh_token = str(token)

            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
                status=status.HTTP_200_OK,
            )
        except KeyError:
            return Response({"message": "Key error"})
