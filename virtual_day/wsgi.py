import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_day.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfiguration')

application = get_wsgi_application()
