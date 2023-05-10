# articles/admin.py

from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_posted', 'author']
    list_filter = ['date_posted', 'author']
    search_fields = ['title', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'text', 'author', 'date_posted']
    list_filter = ['post__date_posted', 'author']
    search_fields = ['text']
