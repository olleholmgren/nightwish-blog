from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0, 'Draft'), 
    (1, 'Published')
)

class Post(models.Model):
    
    post_title = models.CharField(max_length=100, unique=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.post_title

    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.id)])

class Comment(models.Model):

    post_title = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    member = models.CharField(max_length=80)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.member}'

class FavouriteAlbum(models.Model):

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=80)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Album {self.album_title} by {self.member}'
