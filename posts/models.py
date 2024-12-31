from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()   # for text input
    slug = models.SlugField()   # useful to automatically prepopulate a SlugField based on the value of some other value.
    date = models.DateTimeField(auto_now_add=True) # to create time stamps
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # add logged in user as the post author
    
    def __str__(self):
        return self.title
    