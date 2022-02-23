from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    post_title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="What's up? Travel and Lifestyle blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #featured_image = CloudinaryField('image', default='placeholder')
    #category = models.CharField(max_length=255, default="Romance")
    #likes = models.ManyToManyField(User, related_name="blog_posts")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


