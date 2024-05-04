from django.urls import path
from rest_framework import routers

from . import views
from accounts.models.profile import Profile
from accounts.models.user import CustomUser

app_name = "api-v1"


router = routers.DefaultRouter()
router.register('user', views.UserAdminViewSet, basename='user')

urlpatterns = [
    path('profile/', views.ProfileListAPIView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.ProfileRetrieveAPIView.as_view(), name='profile-detail'),
    
]

urlpatterns += router.urls