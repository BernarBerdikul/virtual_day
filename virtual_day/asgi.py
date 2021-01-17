import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_day.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfiguration')

application = get_asgi_application()
