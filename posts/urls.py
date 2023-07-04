from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('post', views.PostCreateView.as_view(), name="post_create"),
    path('my-posts', views.MyPostView.as_view(), name="my_posts"),
    path('my-likes', views.LikedPostView.as_view(), name="my_likes"),
    path('like-toggle/<int:pk>', views.LikeToggleView.as_view(), name="like_toggle"),
    path('my-comments', views.CommentsPostView.as_view(), name="my_comments_list"),
    path('my-comments/<int:pk>', views.CommentDetailView.as_view(), name="my_comments_detail"),
]