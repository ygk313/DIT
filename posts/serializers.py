from rest_framework import serializers
from .models import Like, Post, Comment

# BasePostSerializer
class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user']

# BaseCommentSerializer
class BaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# get Posts commented by user
class CommentSerializer(BaseCommentSerializer):
    post = BasePostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

# Main, Post detail 
class PostSerializer(BasePostSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    comments = BaseCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields =  "__all__"

#  get Posts liked by user
class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = '__all__'
