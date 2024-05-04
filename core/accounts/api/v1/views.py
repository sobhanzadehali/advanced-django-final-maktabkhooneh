from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import ProfileSerializer,CustomUserSerializer
from accounts.models.profile import Profile
from accounts.models.user import CustomUser
from .permissions import IsOwnerOrReadOnly



class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Profile.objects.all()

class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    queryset = Profile.objects.all()


class UserAdminViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser,]
    queryset = CustomUser.objects.all()
    
    