from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ProfileSerializer,CustomUserSerializer
from accounts.models.profile import Profile
from accounts.models.user import CustomUser
from .permissions import IsOwnerOrReadOnly



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
    
    