from django.urls import path
from . import views

app_name = 'front'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('director', views.director, name='director'),
]
