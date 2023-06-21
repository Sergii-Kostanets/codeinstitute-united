from . import views
from django.urls import path
from django.conf.urls import handler404
from django.conf import settings

handler404 = 'connect.views.page_not_found_local'

urlpatterns = [
    path('', views.GameList.as_view(), name='game_list'),
    path('game-create', views.GameCreate.as_view(), name='game_create'),
    path('game-edit/<slug:slug>/', views.GameUpdate.as_view(), name='game_edit'),
    path('game-delete/<slug:slug>/', views.GameDelete.as_view(), name='game_delete'),
    path('game-publish-list', views.GamePublishList.as_view(), name='game_publish_list'),
    path('game-publish/<int:pk>/', views.GamePublish.as_view(), name='game_publish'),
    path('game-connect/<slug:slug>/', views.GameConnect.as_view(), name='game_connect'),
    path('my-games/', views.GamesOfUser.as_view(), name='game_list_of_user'),
]

if settings.DEBUG:
    urlpatterns += [
        path('404', views.page_not_found_local, name='404'),
    ]
