
from django.urls import path, include

from rest_framework import routers

from blogs.views import BlogViewSet

router = routers.DefaultRouter()

router.register(r'blogs', BlogViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
