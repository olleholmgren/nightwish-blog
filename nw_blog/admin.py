from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('post_title', 'status', 'created_on')
    search_fields = ['post_title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('member', 'content', 'post_title', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('member', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)