"""Defines URL patterns for feed."""
from django.urls import path
from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.index, name='index'),
    # path('upload/', views.upload_image, name='upload_image'),
]
