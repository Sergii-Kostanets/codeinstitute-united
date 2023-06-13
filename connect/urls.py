from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='game_list'),
    path('game_create', views.GameCreate.as_view(), name='game_create'),
]
