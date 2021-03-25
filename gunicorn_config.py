command = '/root/project/env/bin/gunicorn'
pythonpath = '/root/project/virtual_day'
bind = '78.140.223.130:8000'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=virtual_day.settings'
