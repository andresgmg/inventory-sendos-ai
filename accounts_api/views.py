from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import (
    UserSerializer,
    RegisterRequestSerializer,
    LoginRequestSerializer,
    SuccessResponseSerializer,
    LogoutResponseSerializer,
)
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate

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
            token = Token.objects.create(user=user)
            user_serializer = UserSerializer(instance=user)
            return Response(
                {"token": "Token {}".format(token.key), "user": user_serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return self.error_response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    tags=["Auth"],
    get=extend_schema(tags=["Auth"], responses={200: SuccessResponseSerializer}),
)
class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SuccessResponseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


@extend_schema_view(
    tags=["Auth"],
    post=extend_schema(tags=["Auth"], responses={204: LogoutResponseSerializer}),
)
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
