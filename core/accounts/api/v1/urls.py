from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views
from accounts.models.profile import Profile
from accounts.models.user import CustomUser


app_name = "api-v1"


router = routers.DefaultRouter()
router.register("user", views.UserAdminViewSet, basename="user")
router.register("profile", views.ProfileViewSet, basename="profile")

urlpatterns = [
    # verification
    path("verify-email/", views.SendVerificationEmail.as_view(), name="email_verify"),
    path(
        "verify/confirm/<str:token>/",
        views.UserVerificationView.as_view(),
        name="user_verify",
    ),
    # resend activation
    path("verify/resend/", views.SendVerificationEmail.as_view(), name="user_verify"),
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path(
        "change-password/",
        views.ChangePasswordAPIView.as_view(),
        name="change_password",
    ),
]

urlpatterns += router.urls
