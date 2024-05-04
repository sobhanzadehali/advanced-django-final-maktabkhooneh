from rest_framework.viewsets import  ModelViewSet
from blog.models import Post

from . import serializers
from .permissions import IsOwnerOrReadOnly




class PostViewSet(ModelViewSet):
    model = Post
    serializer_class = serializers.PostSerializer
    permission_classes = [IsOwnerOrReadOnly,]

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts