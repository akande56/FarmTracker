from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField
# from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for project."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(
        _("Name of User"), blank=True, max_length=255, help_text="user full name"
    )
    phone = CharField(max_length=11)
    user_address = CharField(max_length=50)
    state = CharField(max_length=20)
    lga = CharField(max_length=20)

    is_farmer = BooleanField(blank=True, default=False)
    is_inspector = BooleanField(blank=True, default=False)

    