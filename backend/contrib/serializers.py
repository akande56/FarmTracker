from rest_framework import serializers
from .models import post
# Create your serializers here.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = post
