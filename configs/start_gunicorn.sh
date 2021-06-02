#!/bin/bash
source /srv/www/env/bin/activate
exec gunicorn -c "/srv/www/virtual_day/gunicorn_config.py" virtual_day.wsgi:application
# gunicorn virtual_day.wsgi:application -b 127.0.0.1:8000 --workers=3