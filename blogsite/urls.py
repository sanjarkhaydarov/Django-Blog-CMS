from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:slug>', views.detail, name='detail'),
    path('create-post', views.createPost, name='create')
]