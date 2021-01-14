from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Event(models.Model):
    year = models.CharField(max_length=4)
    content = models.TextField()
    featured_photo = models.ImageField(default='default.jpg', upload_to='featured_images')

    def __str__(self):
        return self.year
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.featured_photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.featured_photo.path)

class Plane(models.Model):
    name = models.CharField(max_length = 50)
    manufacturer = models.CharField(max_length = 20)
    short_description = models.TextField()
    description = models.TextField()
    featured_photo = models.ImageField(default='default.jpg', upload_to='featured_images')

    first_flight = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.manufacturer} {self.name}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.featured_photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.featured_photo.path)
    
class PlaneVariation(models.Model):
    name = models.CharField(max_length=20)
    base_plane = models.ForeignKey(Plane, related_name='variations', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    featured_photo = models.ImageField(default='default.jpg', upload_to='featured_images')

    def __str__(self):
        return f'{self.base_plane.name}-{self.name}'
    