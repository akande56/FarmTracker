from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Farmer


class FarmerCustomRegistrationSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    farm_name = serializers.CharField(required = True)
    farm_address = serializers.CharField(required = True)

    def get_cleaned_data(self):
        data =  super(FarmerCustomRegistrationSerializer, self).get_cleaned_data()

        extra_data = {
            'farm_name': self.validated_data.get('farm_nname', ''),
            'farm_address': self.validated_data.get('farm_address', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(FarmerCustomRegistrationSerializer, self).save(request)
        user.is_farmer = True
        user.save()
        farmer = Farmer(user = user, farm_name = self.cleaned_data.get('farm_name'), \
        farm_address = self.cleaned_data.get('farm_address')
        )
        farmer.save()
        return user
