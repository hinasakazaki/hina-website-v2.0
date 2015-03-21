"""
WSGI config for hina_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this 
com/en/1.7/howto/deployment/wsgi/
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hina_django.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

from dj_static import Cling

application = Cling(get_wsgi_application())

#OLD


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hina_django.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
