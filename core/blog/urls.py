from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name='post_list'),
    path("<str:slug>/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
]
