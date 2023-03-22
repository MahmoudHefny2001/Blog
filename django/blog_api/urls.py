from django.urls import path
from .views import PostViewSet, PostListDetailFilter#, PostDetail, PostList
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

router = DefaultRouter()
# router.register('', PostList, basename='post')
router.register('', PostViewSet, basename='post')

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('', PostList.as_view(), name='listcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
] + router.urls

