from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='game_list'),
    path('game_create', views.GameCreate.as_view(), name='game_create'),
    path('game_edit/<slug:slug>/', views.GameUpdate.as_view(), name='game_edit'),
    path('game_delete/<slug:slug>/', views.GameDelete.as_view(), name='game_delete'),
    path('game_publish_list', views.GamePublishList.as_view(), name='game_publish_list'),
    path('game_publish/<int:pk>/', views.GamePublish.as_view(), name='game_publish'),
    path('game_connect/<slug:slug>/', views.GameConnect.as_view(), name='game_connect'),
]
