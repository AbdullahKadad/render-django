from django.db import models

class Image(models.Model):
    pixabay_id = models.IntegerField(unique=True)
    tags = models.CharField(max_length=255)
    preview_url = models.URLField()
    large_image_url = models.URLField()
    views = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    user = models.CharField(max_length=255)
    user_image_url = models.URLField()
    
    def __str__(self):
        return self.tags