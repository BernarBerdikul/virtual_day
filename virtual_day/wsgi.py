import os
import sys
from configurations.wsgi import get_wsgi_application

path = '/root/project/virtual_day/'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtual_day.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
