from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('edit/<int:pk>/', views.PostEdit.as_view(), name='post_edit'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    path('publish-list/',
         views.PostPublishList.as_view(), name='post_publish_list'),
    path('publish/<int:pk>/',
         views.PostPublish.as_view(), name='post_publish'),
    path('my-posts/', views.PostListUser.as_view(), name='post_list_user'),
    path('comments/draft/',
         views.DraftCommentList.as_view(), name='draft_comment_list'),
    path('comment/approve/<int:comment_id>/',
         views.ApproveComment.as_view(), name='approve_comment'),
    path('comment/delete/<int:comment_id>/',
         views.DeleteComment.as_view(), name='delete_comment'),
]
