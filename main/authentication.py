from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample


@extend_schema_view(
    post=extend_schema(
        summary="Login with JWT",
        description="Authenticate a user and provide access and refresh tokens.",
        request={
            "application/json": {
                "example": {
                    "username": "user123",
                    "password": "securepassword"
                }
            }
        },
        responses={
            200: {
                "description": "Successful login",
                "examples": {
                    "application/json": {
                        "access_token": "access.jwt.token",
                        "refresh_token": "refresh.jwt.token"
                    }
                }
            },
            401: {"description": "Invalid credentials"},
        },
    )
)
class LoginJWTView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@extend_schema_view(
    post=extend_schema(
        summary="Logout with JWT",
        description="Logout a user by blacklisting the refresh token.",
        request={
            "application/json": {
                "example": {
                    "refresh_token": "refresh.jwt.token"
                }
            }
        },
        responses={
            200: {"description": "Successfully logged out."},
            400: {"description": "Invalid token or error occurred."},
        },
    )
)
class LogoutJWTView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
