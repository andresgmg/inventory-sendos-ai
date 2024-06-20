from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


class RegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {
            "username": {"required": True},
            "email": {"required": True},
            "password": {"required": True},
        }


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class SuccessResponseSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    user = UserSerializer()

    class Meta:
        model = User
        fields = ("token", "user")
