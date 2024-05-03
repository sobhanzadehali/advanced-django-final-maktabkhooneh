from typing import Any
from django.db.models.query import QuerySet
from .forms import PostForm
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


class PostListView(ListView):
    """
    template and CB view for listing Posts
    """
    model =  Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self) -> QuerySet[Any]:
        posts = Post.objects.filter(status=True)
        return posts


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    query_pk_and_slug =True

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(status=True)
    
