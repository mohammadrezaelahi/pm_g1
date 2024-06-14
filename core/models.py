from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField()
    role = models.CharField(max_length=100)


    def get_absolute_url(self):
        pass

    def get_image_url(self):
        if self.avatar:
            return self.avatar.url
        return None

    def __str__(self):
        return self.full_name


class FrontSetting(models.Model):
    about_us_text = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None