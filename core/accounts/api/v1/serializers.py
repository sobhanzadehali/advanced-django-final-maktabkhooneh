from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    image = serializers.ImageField(required=False)
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
    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        valid_data = super().validate(attrs)
        valid_data['email'] = self.user.email
        valid_data['user_id'] = self.user.id
        return valid_data
