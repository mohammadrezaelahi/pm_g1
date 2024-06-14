from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse

from blog.models import Post
from consultation.forms import ConsultationForm
from core.models import Profile, FrontSetting, Skill, WorkHistory, UserSocial, SocialMedia

User = get_user_model()


def index(request):
    profiles = Profile.objects.all()
    front_setting = FrontSetting.objects.first()
    skills = Skill.objects.all()
    posts = Post.objects.all()[:7]
    context = {
        'profiles': profiles,
        'front_setting': front_setting,
        'skills': skills,
        'posts': posts,
    }
    return render(request, 'index.html', context)


def user_detail(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    work_histories = WorkHistory.objects.filter(user=profile)
    socials = UserSocial.objects.filter(user=profile)
    context = {
        'profile': profile,
        'front_setting': FrontSetting.objects.first(),
        'work_histories': work_histories,
        'socials': socials,
    }
    return render(request, 'user_detail.html', context)


def contact_us(request):
    if request.method == 'POST':
        ins = ConsultationForm(request.POST)
        if ins.is_valid():
            ins.save()
        return redirect(reverse('core:index'))

    context = {
        'form': ConsultationForm(),
        'front_setting': FrontSetting.objects.first(),
        'socials': SocialMedia.objects.all(),
    }
    return render(request, 'contact_us.html', context)
