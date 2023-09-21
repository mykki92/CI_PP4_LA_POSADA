from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Class for the database blog model
class Post(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
        )
    slug = models.SlugField(
        max_length=200,
        unique=True
        )
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
        )
    created_on = models.DateTimeField(blank=True)
    updated_on = models.DateTimeField()
    content = models.TextField()
    image = CloudinaryField(
        'image',
        default='placeholder'
        )
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()