command = '/root/project/env/bin/gunicorn'
pythonpath = '/root/project/virtual_day'
bind = '127.0.0.1:8001'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = ["DJANGO_SETTINGS_MODULE=virtual_day.settings",
           "DJANGO_CONFIGURATION=BaseConfiguration",
           'SECRET_KEY="hw^7polec^hp18%%stj8k=$v#gsl#zu$%^%bgg908cswiph^w%"',

           "DB_NAME=virtual_day",
           "DB_USER=virtual_day",
           "DB_PASSWORD=virtual_day",
           "DB_HOST=localhost",
           "DB_PORT=5432",

           "EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'",
           "EMAIL_HOST=smtp.gmail.com",
           "EMAIL_HOST_USER='DaBEERman322@gmail.com'",
           "EMAIL_HOST_PASSWORD=Aisultan12",
           'FROM_EMAIL="default from emall"',
           "EMAIL_PORT=25",

           "LOGS_BASE_DIR=logs",

           "GOOGLE_APPLICATION_CREDENTIALS='/root/project/virtual_day/firebase/ServiceAccount.json'"
           ]
