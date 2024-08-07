
from django.contrib import admin
from django.urls import path, include, re_path #

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('users.urls')),

    path('api/v1/', include('blogs.urls')),

    path('api-documentation/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'), #
]
