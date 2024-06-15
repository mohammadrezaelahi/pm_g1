from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class Svg(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    svg = models.FileField(upload_to='svgs', blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'آقا'),
        ('F', 'خانم'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField()
    role = models.CharField(max_length=100)
    skills = models.ManyToManyField('Skill', blank=True, verbose_name="skills")

    def get_absolute_url(self):
        return reverse_lazy('core:user_detail', args=[str(self.user.username)])

    def get_image_url(self):
        if self.avatar:
            return self.avatar.url
        return None

    def __str__(self):
        return self.full_name


class FrontSetting(models.Model):
    about_us_text = models.TextField(blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    contact_us_footer = models.TextField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None


class WorkHistory(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='work_history',
                             verbose_name="work history",
                             blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name="work title", help_text="work title", blank=True,
                             null=True)
    company = models.CharField(max_length=200, verbose_name="company", help_text="company", blank=True, null=True)
    start_date = models.DateField(verbose_name="start date", help_text="start date", blank=True, null=True)
    end_date = models.DateField(verbose_name="end date", help_text="end date", blank=True, null=True)


class UserSocial(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ducker_socials',
                             verbose_name="ducker socials",
                             blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="title",
                             help_text="social media title")
    social_id = models.CharField(max_length=500, blank=True, null=True, verbose_name="social id",
                                 help_text="social media id")
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name="link",
                            help_text="social media link")
    svg = models.ForeignKey(Svg, related_name='user_social_logo', blank=True, null=True, verbose_name="logo",
                            on_delete=models.SET_NULL, )

    order = models.PositiveSmallIntegerField(verbose_name="icon order",
                                             default=1,
                                             blank=True,
                                             help_text="this number is the position of icon on front"
                                             )

    def get_image_url(self):
        if self.svg.svg:
            return self.svg.svg.url
        return None


    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name="title",
                             help_text="social media title")
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name="link",
                            help_text="social media link")

    order = models.PositiveSmallIntegerField(verbose_name="icon order",
                                             default=1,
                                             blank=True,
                                             help_text="this number is the position of icon on front"
                                             )
    svg = models.ForeignKey(Svg, related_name='social_logo', blank=True, null=True, verbose_name="logo",
                            on_delete=models.SET_NULL, )


    def get_image_url(self):
        if self.svg.svg:
            return self.svg.svg.url
        return None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', ]
