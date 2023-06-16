from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


#Create Member model

# class Member:
#     member_id =
#     member_name = CharField



#Create Post model

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
