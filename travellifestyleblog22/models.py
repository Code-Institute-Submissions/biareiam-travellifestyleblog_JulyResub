from django.db import models
from django.contrib.auth.models import User
#from cloudinary.models import CloudinaryField
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #bio = models.TextField()
    bio = RichTextField(blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/", default="placeholder")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')
    email = models.EmailField(default=' ')


    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    



class Post (models.Model):
    post_title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    #featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #featured_image = CloudinaryField('image', default='placeholder')
    content = RichTextField(blank=True, null=True)
    #content = models.TextField()
    category = models.CharField(max_length=255, default="Movies")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    image = models.ImageField(null=False, blank=False, upload_to="images/", default="placeholder")
 
    

    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.post_title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_addded = models.DateTimeField(auto_now_add=True)
    #likes = models.ManyToManyField(User, related_name="blog_posts")

    class Meta:
        ordering = ["-date_addded"]
    
    def __str__(self):
        return '%s -%s' % (self.post.post_title, self.name)



    