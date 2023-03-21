from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, 
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
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
    

# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


#     def create(self, request):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


# class PostList(generics.ListCreateAPIView): 
#     permission_classes = []
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission): 
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer