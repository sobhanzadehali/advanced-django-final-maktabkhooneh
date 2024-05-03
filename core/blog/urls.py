from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name='post_list'),
    path("<str:slug>/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create/", views.PostCreateview.as_view(), name='create_post'),
    path("update/<str:slug>/<int:pk>/", views.PostUpdateView.as_view(), name="post_update"),
]
