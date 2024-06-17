from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate

@extend_schema_view(
    tags=["Auth"],
    post=extend_schema(tags=["Auth"], request=RegisterSerializer, responses={201: UserSerializer}),
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

@extend_schema_view(
    tags=["Auth"],
    get=extend_schema(tags=["Auth"], responses={200: UserSerializer}),
)
class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

@extend_schema_view(
    tags=["Auth"],
    post=extend_schema(tags=["Auth"], responses={204: None}),
)
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@extend_schema_view(
    tags=["Auth"],
    post=extend_schema(tags=["Auth"], request=None, responses={200: None}),
)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
