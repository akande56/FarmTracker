from django.db import models

# Create your models here.

class post(models.Model):
    """Model definition for post."""
    name = models.CharField(max_length=50)
    class Meta:
        """Meta definition for post."""

        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        """Unicode representation of post."""
        return str(self.name)
