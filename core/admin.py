from django.contrib import admin

from core.models import Profile, FrontSetting, Skill


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name']



admin.site.register(FrontSetting)
admin.site.register(Skill)

