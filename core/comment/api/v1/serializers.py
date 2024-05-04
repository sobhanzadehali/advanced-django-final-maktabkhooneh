from rest_framework import serializers 
from comment.models import Comment
from blog.models import Post

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False,read_only=True,slug_field='user__email')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    status = serializers.ReadOnlyField()


    class Meta:
        model = Comment
        fields = ('id','post', 'author', 'body', 'created_date', 'status',)