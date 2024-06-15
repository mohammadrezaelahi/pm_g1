# Generated by Django 5.0.6 on 2024-06-15 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Svg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='usersocial',
            name='logo',
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='svg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social_logo', to='core.svg', verbose_name='logo'),
        ),
        migrations.AddField(
            model_name='usersocial',
            name='svg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_social_logo', to='core.svg', verbose_name='logo'),
        ),
    ]