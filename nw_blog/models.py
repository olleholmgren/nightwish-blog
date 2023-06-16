from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


#Create Member model

# class Member:
#     member_id =
#     member_name = CharField



#Create Post model

class Post(models.Model):
    post_title = models.CharField(max_length=100, unique=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return f'{self.title} | {self.author}'

