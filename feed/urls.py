"""Defines URL patterns for feed."""
from django.urls import path
from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.index, name='home'),
    # path('upload/', views.upload_image, name='upload_image'),
]
