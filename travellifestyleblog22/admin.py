from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('post_title', 'category', 'created_on')
    list_filter = ('category', 'created_on',)
    search_fields = ('post_title', 'category',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_addded',)

admin.site.register(Category)