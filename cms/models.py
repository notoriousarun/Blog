from django.db import models as models
from django.db.models import CharField, ImageField, TextField
from django.conf import settings
from taggit.managers import TaggableManager


class BlogPost(models.Model):

    # Fields
    page_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="upload/images/")
    content = models.TextField()
    meta_title = models.CharField(max_length=60)
    meta_description = models.CharField(max_length=160)
    category = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    # Relationship Fields
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="blogposts",
    )

    tags = TaggableManager()

    class Meta:
        ordering = ('-pk',)
