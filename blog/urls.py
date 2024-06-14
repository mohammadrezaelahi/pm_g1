from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.all_posts, name='home'),
]