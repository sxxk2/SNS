from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.account.models import Account


# api/v1/accounts/signup
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "name",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        account = Account.objects.create_user(**validated_data)
        account.set_password(validated_data.get("password"))
        account.save()
        return account


# api/v1/accounts/signin
class SignInSerializer(TokenObtainPairSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "password",
        ]

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if Account.objects.filter(email=email).exists():
            account = Account.objects.get(email=email)

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
