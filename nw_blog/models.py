from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.urls import reverse

STATUS = (
    (0, 'Draft'), 
    (1, 'Published')
)

class Post(models.Model):
    
    post_title = models.CharField(max_length=100, unique=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post_title} | {self.post_author} | {self.content}'

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):

    post_title = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.post_author} on {self.post_title}'
    
    # def get_absolute_url(self):
    #      return reverse('post_view', args=(str(self.id)))