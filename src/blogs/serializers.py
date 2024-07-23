from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        exclude = ['modified']
        read_only_fields = ['user']
    

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = instance.user.username
        return response