from django.urls import path
from .views import InspectorRegistrationView


urlpatterns = [
    path('registration/', InspectorRegistrationView.as_view(), name='register-inspector'),
]