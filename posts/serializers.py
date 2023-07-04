
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
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
    comment_set = BaseCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields =  "__all__"

# Create Post 
class PostCreateSerializer(BasePostSerializer):
    title = serializers.CharField()
    content = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'user']



#  BaseLikeSerializer
class BaseLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

# LikeSerializer
class LikeSerializer(BaseLikeSerializer):
    post = PostSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = '__all__'
