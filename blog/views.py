from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from blog.models import Post
from core.models import FrontSetting


def all_posts(request):

    posts = Post.objects.all()
    total_views = posts.aggregate(total=Sum('views'))['total']

    context = {
        'front_setting': FrontSetting.objects.first(),
        'posts': posts,
        'total_views': total_views,
    }
    return render(request, 'all_posts.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'front_setting': FrontSetting.objects.first(),
        'post': post,
    }
    return render(request, 'post_detail.html', context)