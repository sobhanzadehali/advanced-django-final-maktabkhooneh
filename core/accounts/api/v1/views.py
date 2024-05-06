from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model


from .serializers import ProfileSerializer,CustomUserSerializer, CustomTokenObtainPairSerializer,ChangePasswordSerializer
from accounts.models.profile import Profile
from accounts.models.user import CustomUser
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Profile.objects.all()
    parser_classes = [MultiPartParser, FormParser,]
    http_method_names = ('get','post', 'put', 'patch', 'head')


class UserAdminViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser,]
    queryset = CustomUser.objects.all()
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.UpdateAPIView):
    model = User
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer
    http_method_names = ['put']

    def get_object(self):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': 'wrong password!'})
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({"detail": "password changed"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    