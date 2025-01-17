from django.db import models
from django.conf import settings 

class Article(models.Model):
    title = models.CharField(max_length=200)  
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()  
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    published = models.DateTimeField(auto_now_add=True)  
    is_published = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.title
