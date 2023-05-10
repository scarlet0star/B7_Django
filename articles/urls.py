# articles/urls.py

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/posts/', views.PostListAPIView.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail_api'),
    path('api/posts/<int:post_id>/comments/', views.CommentListAPIView.as_view(), name='comment_list_api'),
    path('api/posts/<int:post_id>/comments/<int:pk>/', views.CommentDetailAPIView.as_view(), name='comment_detail_api'),
    path('', views.post_list, name='post_list'),  # post_list view 등록
]

urlpatterns = format_suffix_patterns(urlpatterns)




