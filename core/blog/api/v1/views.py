from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from blog.models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
    ]
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts

    def get_parsers(self):
        if getattr(self, "swagger_fake_view", False):
            return []
        return super().get_parsers()
