from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'liked_users', 'image', 'created_at', 'updated_at', 'comments']

