from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views
from accounts.models.profile import Profile
from accounts.models.user import CustomUser


app_name = "api-v1"


router = routers.DefaultRouter()
router.register("user", views.UserAdminViewSet, basename="user")
router.register("profile", views.ProfileViewSet, basename="profile")

urlpatterns = [
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),

]

urlpatterns += router.urls
