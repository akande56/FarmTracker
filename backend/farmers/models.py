from django.db import models
from user.models import User


class Farmer(models.Model):
    """Model definition for Farmer."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    farm_name = models.CharField(max_length=50, blank=True, default="farm name",null=True, unique=True)
    farm_address = models.CharField(max_length=50, blank=True,default="farm address" )

    class Meta:
        """Meta definition for Farmer."""

        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"

    def __str__(self):
        """Unicode representation of Farmer."""
        return str(self.user.username)