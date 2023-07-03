from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from .models import Post, Like, Comment
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts import serializers

# ----- Posts Area ------

# main에 돌려주기 위해 필요한 view
class MainPostView(APIView):

    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

# pk에 따른 Post 디테일 내용을 확인하기 위한 View
class PostDetailView(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # 일부 업데이트를 위해 PATCH 사용.
    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        # serializer.is_valid()는 들어간 형식이 올바른지 확인하기 위함.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Posts written by user
class MyPostView(APIView):

    def get(self, request, format=None):
        posts = Post.objects.filter(user=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# ----- Likes Area ------

# Posts user liked
class LikedPostView(APIView):

    def get(self, request, format=None):
        likes = Like.objects.filter(user = request.user)
        serializer = LikeSerializer(likes, many=True)

        return Response(serializer.data)

class LikeToggleView(APIView):
    
    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        post_like, post_like_created = post.like_set.get_or_create(user=request.user)

        if post_like_created:
            return Response("like", status = status.HTTP_201_CREATED)
        else:
            post_like.delete()
            return Response("unllike", status = status.HTTP_404_NOT_FOUND)

# ----- Comments Area ------

# Posts user commented
class CommentsPostView(APIView):

    def get(self, request, format=None):
        comments = Comment.objects.filter(user=request.user)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BaseCommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

# comment - DELETE
class CommentDetailView(APIView):

    def delete(self, request, pk, format = None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)