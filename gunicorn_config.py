command = '/root/project/env/bin/gunicorn'
pythonpath = '/root/project/project_name'  # project_name
bind = '127.0.0.1:8000'  # ip_address
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=project_name.settings'  # project_name
