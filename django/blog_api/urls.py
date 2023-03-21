from django.urls import path
from .views import PostViewSet #, PostList, PostDetail
from rest_framework.routers import DefaultRouter


app_name = 'blog_api'

router = DefaultRouter()
# router.register('', PostList, basename='post')
router.register('', PostViewSet, basename='post')
urlpatterns = router.urls

# urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('', PostList.as_view(), name='listcreate'),
# ]

