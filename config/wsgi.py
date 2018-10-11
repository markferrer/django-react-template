"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

# Using configurations instead of django.core.wsgi
# in order to make use of a class-based settings file.
from configurations.wsgi import get_wsgi_application


configuration = os.getenv('ENVIRONMENT', 'dev').title()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', configuration)

application = get_wsgi_application()
