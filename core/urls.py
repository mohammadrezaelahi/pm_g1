from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('', views.index, name='index'),
]