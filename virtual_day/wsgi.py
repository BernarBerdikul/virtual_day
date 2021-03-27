import os
import sys
from configurations.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

path = '/root/project/virtual_day/'
if path not in sys.path:
    sys.path.append(path)

print(os.getenv('DJANGO_SETTINGS_MODULE'))
print(os.getenv('DJANGO_CONFIGURATION'))

os.environ.setdefault(os.getenv('DJANGO_SETTINGS_MODULE'), 'virtual_day.settings')
os.environ.setdefault(os.getenv('DJANGO_CONFIGURATION'), 'Dev')

application = get_wsgi_application()
