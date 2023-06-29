from rest_framework import serializers
from .models import Like, Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields =  "__all__"

class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = '__all__'