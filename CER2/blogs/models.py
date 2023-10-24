from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    overview = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.author:
            # Set the author to a default user or the currently logged-in user
            self.author = User.objects.get(username='your_default_author_username')
        super().save(*args, **kwargs)
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True) 
    
    class Meta:
        verbose_name_plural = 'categories'
        
        
    def __str__(self):
        return self.title
    