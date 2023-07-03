from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('<int:pk>', views.PostDetailView.as_view()),
    path('my-posts', views.MyPostView.as_view()),
    path('my-likes', views.LikedPostView.as_view()),
    path('my-comments', views.CommentsPostView.as_view()),
]