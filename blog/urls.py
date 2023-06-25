from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('edit/<int:pk>/', views.PostEdit.as_view(), name='post_edit'),
]
