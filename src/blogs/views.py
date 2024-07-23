from rest_framework.viewsets import ModelViewSet

from .models import Blog

from .serializers import BlogSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authentication import TokenAuthentication

from .permissions import IsOwner

from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import SAFE_METHODS

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [AllowAny()]
        else:
            return [
                IsAuthenticated(), 
            ]

    # handle updating, and deleting a blog to be only for the user who created it
    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("You do not have permission to edit this blog.")
        serializer.save()
    
    def partial_update(self, request, *args, **kwargs):
        blog = self.get_object()
        if request.user != blog.user:
            raise PermissionDenied("You do not have permission to edit this blog.")
        return super().partial_update(request, *args, **kwargs)

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise PermissionDenied("You do not have permission to delete this blog.")
        instance.delete()


    def get_queryset(self):
        return super().get_queryset().order_by('-created')
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    