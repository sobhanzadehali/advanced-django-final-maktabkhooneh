from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("api/v1/", include("accounts.api.v1.urls")),
]
