from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('blog/', views.blog, name='blog'),
    # path('blog/<int:post_id>/', views.blog_post, name='blog_post'),
]