from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='game_list'),
    path('game_create', views.GameCreate.as_view(), name='game_create'),
    path('game_edit/<slug:slug>/', views.GameUpdate.as_view(), name='game_edit'),
]
