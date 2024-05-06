from rest_framework import serializers
from datetime import datetime

from blog.models import Post, Category
from accounts.models.profile import Profile
from accounts.api.v1.serializers import ProfileSerializer
from comment.api.v1.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="user__email"
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )
    banner = serializers.ImageField(required=False)
    status = serializers.ReadOnlyField()
    comment = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "slug",
            "category",
            "banner",
            "body",
            "comment",
            "status",
            "updated_date",
            "created_date",
        )

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user=self.context.get("request").user.id
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_date"] = datetime.now()
        validated_data["status"] = False
        return super().update(instance, validated_data)


class CategorySerializer(serializers.ModelSerializer):
    post_list = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
