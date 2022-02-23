from django.db import models
from django.contrib.auth.models import User
#from cloudinary.models import CloudinaryField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, default='Mary')
    last_name = models.CharField(max_length=255, default='Ann')
    email = models.EmailField(default='my@email.com')


    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    
    def save(self):
      super().save()


class Post (models.Model):
    post_title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    #featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    category = models.CharField(max_length=255, default="Movies")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    image = models.ImageField(null=True, blank=True, upload_to="images/")
 
    

    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.username)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()



    