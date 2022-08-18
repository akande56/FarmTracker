from rest_auth.registration.views import RegisterView
from .serializers import InspectorCustomRegistrationSerializer



class InspectorRegistrationView(RegisterView):
    serializer_class = InspectorCustomRegistrationSerializer