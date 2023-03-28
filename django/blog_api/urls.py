from django.urls import path
from .views import (PostViewSet, PostListDetailFilter,  
    CreatePost, EditPost, DeletePost, AdminPostDetail)
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostViewSet, basename='post')

urlpatterns = [
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),

    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),

] + router.urls

