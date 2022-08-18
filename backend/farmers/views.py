from rest_auth.registration.views import RegisterView
from .serializers import FarmerCustomRegistrationSerializer



class FarmerRegistrationView(RegisterView):
    serializer_class = FarmerCustomRegistrationSerializer