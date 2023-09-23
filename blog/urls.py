from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .import views
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('category',views.category,name="category"),
    #path('singel',views.singel,name="singel"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

