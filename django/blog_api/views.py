from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, 
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
)
from rest_framework import viewsets, filters

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    # queryset = Post.postobjects.all()

    def get_object(self, queryset=None, **kwargs): 
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


    def get_queryset(self):
        return Post.objects.all()


class PostListDetailFilter(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']
