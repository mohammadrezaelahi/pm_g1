from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse_lazy

from core.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    views = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    def get_absolute_url(self):
        return reverse_lazy('blog:post_detail', args=[self.id,])


