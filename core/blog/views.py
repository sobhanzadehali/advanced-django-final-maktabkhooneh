from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
from accounts.models.profile import Profile

# Create your views here.


class PostListView(ListView):
    """
    template and CB view for listing Posts
    """

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self) -> QuerySet[Any]:
        posts = Post.objects.filter(status=True)
        return posts


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    query_pk_and_slug = True

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(status=True)


class PostCreateview(CreateView,PermissionRequiredMixin):
    model = Post
    permission_required = 'blog.add_post'
    fields = ("title", "slug", "banner", "body", "category")
    template_name = "blog/post_create.html"
    

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.author = Profile.objects.create(user=self.request.user)
        return super().form_valid(form)

class PostUpdateView(UpdateView, PermissionRequiredMixin):
    model = Post
    template_name = 'blog/post_update.html'
    permission_required = 'blog.change_post'
    permission_denied_message = ' you dont have the permission to edit a post in blog'
    fields = ('title', 'slug', 'banner', 'body',)
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(author__user=self.request.user)

