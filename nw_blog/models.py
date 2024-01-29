from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _


STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)


class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,
                                   related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


class FavouriteAlbum(models.Model):

    author = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE,
                               related_name='favourite_album')
    

    class AlbumChoices(models.TextChoices):

        CHOOSE_AN_ALBUM = ('Choose an album')
        ANGELS_FALL_FIRST = ('Angels Fall First')
        OCEANBORN = ('Oceanborn')
        WISHMASTER = ('Wishmaster')
        CENTURY_CHILD = ('Century Child')
        ONCE = ('Once')
        DARK_PASSION_PLAY = ('Dark Passion Play')
        IMAGINAERUM = ('Imaginaerum')
        ENDLESS_FORMS_MOST_BEAUTIFUL = ('Endless Forms Most Beautiful')
        HUMAN_NATURE = ('Human. :||: Nature.')

    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    favourite_album = models.CharField(
        max_length=30,
        choices=AlbumChoices.choices,
        default=AlbumChoices.CHOOSE_AN_ALBUM,
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.favourite_album
