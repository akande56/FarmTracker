from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Inspector


class InspectorCustomRegistrationSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    def save(self, request):
        user = super(InspectorCustomRegistrationSerializer, self).save(request)
        user.is_inspector = True
        user.save()
        inspector = Inspector(user = user)
        inspector.save()
        return user
