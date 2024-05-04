from rest_framework.serializers import ModelSerializer

from accounts.models.profile import Profile




class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__',)