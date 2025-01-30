from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)  
    content = RichTextField()  
    image = models.ImageField(upload_to='pages_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    biography = models.TextField(blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
