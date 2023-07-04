from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from django.db.models.fields import related
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager

# Table: 포스트
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    liked_users = models.ManyToManyField(User, blank=True, related_name="liked_users", through='Like')
    image = models.FileField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def summary(self):
        return self.content[:25]
        
    @property
    def comments(self):
        return Comment.objects.filter(post=self)
    
    @property
    def like_counts(self):
        return self.liked_users.count()


#Table: 댓글
class Comment(models.Model):
    class Meta:
        ordering = ['-created_at']
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Table: Like
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name="like_toggle_constraint")
        ]


