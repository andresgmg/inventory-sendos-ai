from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import (
    UserSerializer,
    RegisterRequestSerializer,
    LoginRequestSerializer,
    SuccessResponseSerializer,
)
from drf_spectacular.utils import extend_schema


# Base de todas las views para homologar los mensajes de errores
from utils.views import BaseView


class RegisterView(BaseView):

    @extend_schema(
        tags=["Auth"],
        description="Register a new user.",
        request=RegisterRequestSerializer,
        responses={201: UserSerializer, 400: "Bad Request"},
    )
    def post(self, request):
        serializer = RegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            user_serializer = UserSerializer(instance=user)
            return Response(
                {"token": "You have to Login first!", "user": user_serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return self.error_response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginView(BaseView):

    @extend_schema(
        tags=["Auth"],
        description="Login with username and password",
        request=LoginRequestSerializer,
        responses={200: SuccessResponseSerializer},
    )
    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(
                User,
                username=serializer.validated_data["username"],
            )
            if user.check_password(serializer.validated_data["password"]):
                token, _ = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(instance=user)
                return Response(
                    {
                        "token": "Token {}".format(token.key),
                        "user": user_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                # Manually documenting the exception
                return Response(
                    {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return self.error_response(serializer.errors, status.HTTP_400_BAD_REQUEST)
