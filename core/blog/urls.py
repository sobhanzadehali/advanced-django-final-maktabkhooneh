from django.urls import path, include
from django.views.decorators.cache import cache_page
from . import views

app_name = "blog"

urlpatterns = [
    # template view urls
    path("index/", cache_page(60*5)(views.index), name="index"),
    path("", cache_page(60*5)(views.PostListView.as_view()), name="post_list"),
    path("<str:slug>/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create/", views.PostCreateview.as_view(), name="create_post"),
    path(
        "update/<str:slug>/<int:pk>/",
        views.PostUpdateView.as_view(),
        name="post_update",
    ),
    path(
        "delete/<str:slug>/<int:pk>/",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),
    # api view urls
    path("api/v1/", include("blog.api.v1.urls")),
]
