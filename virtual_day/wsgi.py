import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menushka.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfiguration')

from configurations import importer
importer.install()
django.setup()

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
