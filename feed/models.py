from django.db import models 
from sorl.thumbnail import ImageField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False,null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = ImageField(blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title