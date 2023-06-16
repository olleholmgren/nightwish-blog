from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('post_title',)}
    summernote_fields = ('content')


