from django.urls import path
from rest_framework import routers

from . import views
from accounts.models.profile import Profile
from accounts.models.user import CustomUser

app_name = "api-v1"


router = routers.DefaultRouter()
router.register('user', views.UserAdminViewSet, basename='user')
router.register('profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    
    
]

urlpatterns += router.urls