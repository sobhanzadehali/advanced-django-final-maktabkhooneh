from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import ScopedRateThrottle
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import jwt


from .serializers import (
    ProfileSerializer,
    CustomUserSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
)
from accounts.models.profile import Profile
from accounts.models.user import CustomUser
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
    ]
    queryset = Profile.objects.all()
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]
    http_method_names = ("get", "post", "put", "patch", "head")


class UserAdminViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [
        IsAdminUser,
    ]
    queryset = CustomUser.objects.all()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.UpdateAPIView):
    model = User
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ChangePasswordSerializer
    http_method_names = ["put"]

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "wrong password!"})
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"detail": "password changed"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendVerificationEmail(generics.GenericAPIView):
    throttle_scope = "email"
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        if request.user.is_verified:
            return Response(
                {"detail": "your account is already verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.user_obj = self.request.user
        tokens = self.get_tokens_for_user(self.user_obj)

        mail_txt = f"verify your account:\n\n \
            http://localhost:8000/accounts/api/v1/activate/confirm/{tokens['access']}/"

        send_mail(
            "Subject here",
            mail_txt,
            "from@example.com",
            [self.user_obj.email],
            fail_silently=False,
        )
        return Response(f"email sent {request.method}")

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


class UserVerificationView(APIView):

    def get(self, request, token, *args, **kwargs):
        try:

            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            return Response(
                {"detail": "token expired!"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.InvalidSignatureError:
            return Response(
                {"detail": "signature is invalid"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(id=token["user_id"])
        if user.is_verified:
            return Response({"detail": "user is already verified."})
        user.is_verified = True
        user.save()
        return Response(
            {"detail": "user account verification completed"},
            status=status.HTTP_202_ACCEPTED,
        )


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)