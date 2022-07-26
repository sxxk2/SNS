from rest_framework import serializers

from apps.account.models import Account


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
        # email = validated_data.get("email")
        # nickname = validated_data.get("nickname")
        # password = validated_data.get("password")
        account = Account.objects.create_user(**validated_data)
        account.set_password(validated_data.get("password"))
        account.save()
        return account
