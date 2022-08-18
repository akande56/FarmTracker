from django.db import models
from user.models import User


class Inspector(models.Model):
    """Model definition for Inspector."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    class Meta:
        """Meta definition for Inspector."""

        verbose_name = "Inspector"
        verbose_name_plural = "Inspectors"

    def __str__(self):
        """Unicode representation of Inspector."""
        return str(self.user.username)