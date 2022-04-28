from django.contrib import admin
from .models import Post, Category, Comment, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('post_title', 'category', 'created_on')
    list_filter = ('category', 'created_on',)
    search_fields = ('post_title', 'category')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'created_on')

admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_addded')
