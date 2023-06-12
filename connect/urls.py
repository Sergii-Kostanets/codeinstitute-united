from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='game_list'),
    path('edit/<slug:slug>', views.GameEdit.as_view(), name='game_edit'),
]
