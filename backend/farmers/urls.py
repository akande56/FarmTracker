from django.urls import path
from .views import FarmerRegistrationView


urlpatterns = [
    path('registration/', FarmerRegistrationView.as_view(), name='register-farmer'),
]