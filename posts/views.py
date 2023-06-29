from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# main에 돌려주기 위해 필요한 view
class MainPostView(APIView):

    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)

        return Response(serializer.data)