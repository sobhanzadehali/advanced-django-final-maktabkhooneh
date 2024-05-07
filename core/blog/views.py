from django.shortcuts import render
from django.urls import reverse_lazy
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import PostForm
from accounts.models.profile import Profile
from accounts.forms import SubForm
from comment.forms import CommentForm
from comment.views import CommentFormView

# Create your views here.


def index(request):
    return render(request, "index.html")


class PostListView(ListView):
    """
    template and CB view for listing Posts
    """

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = SubForm()
        return data

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        form = CommentForm(request.POST)
        # Set the current user
        # to the comment_author field
        form.instance.author = Profile.objects.get(user=request.user)
        # Set the blog post as the current blogpost
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.status = False
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)



class PostCreateview(CreateView, PermissionRequiredMixin):
    model = Post
    permission_required = "blog.add_post"
    fields = ("title", "slug", "banner", "body", "category")
    template_name = "blog/post_create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class PostUpdateView(UpdateView, PermissionRequiredMixin):
    model = Post
    template_name = "blog/post_update.html"
    permission_required = "blog.change_post"
    permission_denied_message = " you dont have the permission to edit a post in blog"
    fields = (
        "title",
        "slug",
        "banner",
        "body",
    )

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(author__user=self.request.user)


class PostDeleteView(DeleteView, PermissionRequiredMixin):
    model = Post
    template_name = "blog/post_delete.html"
    permission_required = "blog.delete_post"
    permission_denied_message = " you dont have the permission to delete this post"
    success_url = reverse_lazy("blog:post_list")
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(author__user=self.request.user)
