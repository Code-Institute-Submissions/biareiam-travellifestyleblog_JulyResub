from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
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
        return reverse('home')


