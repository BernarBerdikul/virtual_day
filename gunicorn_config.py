command = '/srv/www/env/bin/gunicorn virtual_day.wsgi:application'
pythonpath = '/srv/www/virtual_day'
bind = '127.0.0.1:8001'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = ["DJANGO_SETTINGS_MODULE=virtual_day.settings"]