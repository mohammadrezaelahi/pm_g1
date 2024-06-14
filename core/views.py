from django.shortcuts import render

from core.models import Profile, FrontSetting, Skill
def index(request):
    profiles = Profile.objects.all()
    front_setting = FrontSetting.objects.first()
    skills = Skill.objects.all()
    context = {
        'profiles': profiles,
        'front_setting': front_setting,
        'skills': skills,
    }
    return render(request, 'index.html', context)
