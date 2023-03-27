from django.shortcuts import render, get_object_or_404
from rest_framework import generics, views
from rest_framework.response import Response
from blog.models import Post, Category
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, 
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, AllowAny
)
from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, FormParser

from django.views.decorators.csrf import csrf_exempt


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs): 
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


    def get_queryset(self):
        return Post.objects.all()


class CreatePost(views.APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @csrf_exempt
    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListDetailFilter(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug', '^title']



class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()