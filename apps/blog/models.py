from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="category_posts")
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"