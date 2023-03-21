from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html')),
]