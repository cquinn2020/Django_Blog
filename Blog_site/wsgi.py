"""
WSGI config for Blog_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog_site.settings')

application = get_wsgi_application()

# wisgi is how our python web app and the web server communicate
# django set up simple default 