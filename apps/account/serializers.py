from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.account.models import Account


# api/v1/accounts/signup
class SignUpSerializer(ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        account.set_password(validated_data.get("password"))
        account.save()
        return account

    class Meta:
        model = Account
        fields = [
            "email",
            "account_name",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}


# api/v1/accounts/signin
class SignInSerializer(TokenObtainPairSerializer):
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if Account.objects.filter(email=email).exists():
            account = Account.objects.get(email=email)

            if not account.is_active:
                raise serializers.ValidationError("삭제된 계정입니다.")

            if not account.check_password(password):
                raise serializers.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")  # 비밀번호 틀림
        else:
            raise serializers.ValidationError("아이디 또는 비빌먼호를 잘못 입력했습니다.")  # 아이디 없음

        token = super().get_token(account)
        access_token = str(token.access_token)
        refresh_token = str(token)

        data = {
            "access": access_token,
            "refresh": refresh_token,
        }
        return data

    class Meta:
        model = Account
        fields = [
            "email",
            "password",
        ]


# api/v1/accounts/<int:pk>
class AccountDetailSerializer(ModelSerializer):
    def validate(self, data):
        account_name = data.get("account_name")

        if Account.objects.filter(account_name=account_name).exists():
            raise serializers.ValidationError("이미 사용중인 사용자 이름입니다.")

        return data

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.save()
        return user

    class Meta:
        model = Account
        fields = [
            "id",
            "account_name",
            "user_name",
            "bio",
            "website",
            "profile_image",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/v1/accounts/<int:pk>
class AccountDeleteSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if not instance.is_active:
            raise serializers.ValidationError("이미 삭제된 유저입니다.")
        instance.is_active = False
        instance.deleted_at = datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Account
        fields = [
            "id",
            "is_active",
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}
