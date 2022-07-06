import os

from .base import *

SECRET_KEY = 'fkEqzDxVkofFVSGrpixI0FaVf5xpqebcOLWIj/vKkTf43y/cQ2nqXPOY80uYuh+B3i5n7/YvzbS5voRG65vbFw=='
DEBUG = False
ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST")]


# White Noise configuration - http://whitenoise.evans.io/en/stable/django.html
INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# Must insert after SecurityMiddleware, which is first in settings/common.py
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "frontend", "build")]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "../", "frontend", "build", "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
WHITENOISE_ROOT = os.path.join(BASE_DIR, "../", "frontend", "build", "root")
