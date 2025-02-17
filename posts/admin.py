from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
