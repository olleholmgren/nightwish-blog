from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


# Create Member model
# class Member:
#     member_id =
#     member_name = CharField



#Create Post model

class Post(models.Model):
    
    post_title = models.CharField(max_length=100, unique=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='')
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
    content = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.post_author} on {self.post_title} at {self.created_on}'