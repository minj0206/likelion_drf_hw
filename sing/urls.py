from .views import *
from django.urls import path
from . import views

app_name = 'sing'

urlpatterns = [
    path('singers/', views.singer_list_create, name='singer-list-create'),
    path('songs/', views.song_list_create, name='song-list-create'),
]
