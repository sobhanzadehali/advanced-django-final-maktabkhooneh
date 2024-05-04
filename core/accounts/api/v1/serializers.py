from rest_framework import serializers

from accounts.models.profile import Profile
from accounts.models.user import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
        )


class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "image",
            "description",
        )
