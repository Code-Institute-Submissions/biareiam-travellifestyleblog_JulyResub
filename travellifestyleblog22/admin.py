from django.contrib import admin
from .models import Post, Category, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
