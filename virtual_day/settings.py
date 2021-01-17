import os
from configurations import Configuration
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'virtual_day')


class BaseConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = os.getenv('SECRET_KEY')

    DEBUG = True

    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Django Rest Framework
        'rest_framework',
        'rest_framework.authtoken',

        # DRF API logging
        'drf_api_logger',

        # core header
        'corsheaders',

        # Project apps
        'virtual_day.users',
        'virtual_day.blog',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsPostCsrfMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # DRF logger middleware
        'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',
    ]

    DRF_API_LOGGER_DATABASE = True

    X_FRAME_OPTIONS = 'DENY'

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 300

    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True

    ROOT_URLCONF = 'virtual_day.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(PROJECT_DIR, 'templates'), ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'virtual_day.wsgi.application'

    # Channels
    # ASGI_APPLICATION = 'virtual_day'

    # AUTH_USER_MODEL = 'users.User'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'CONN_MAX_AGE': 60 * 10,  # 10 minutes
        }
    }

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
            'rest_framework.permissions.DjangoModelPermissions',
        ),
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_AUTHENTICATION_CLASSES': (

            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_THROTTLE_CLASSES': [
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ],
        'DEFAULT_THROTTLE_RATES': {
            'anon': '12/second',
            'user': '12/second',
        },
        'EXCEPTION_HANDLER': 'virtual_day.utils.exceptions.custom_exception_handler',
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    CACHES = {
        "default": {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'virtual_day_cache',
        },
    }

    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        # "ip_address",
    ]

    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'PATCH',
        'POST',
        'PUT',
    ]

    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]

    LANGUAGE_CODE = 'ru-RU'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
    STATICFILES_DIRS = (
        # ('css', os.path.join(STATIC_ROOT, 'css')),
        # ('js', os.path.join(STATIC_ROOT, 'js')),
        # ('images', os.path.join(STATIC_ROOT, 'images')),
        # "/static",
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    SITE_URL = 'http://127.0.0.1:8000'

    LOGS_BASE_DIR = os.getenv('LOGS_BASE_DIR', os.getenv('LOGS_BASE_DIR'))

    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'formatters': {
    #         'console': {
    #             'format': '%(name)-12s %(levelname)-8s %(message)s'
    #         },
    #         'verbose': {
    #             'format': '[%(levelname)s] %(asctime)s path: %(pathname)s module: %(module)s method: %(funcName)s  row: %(lineno)d message: %(message)s'
    #         },
    #     },
    #     'handlers': {
    #         'console': {
    #             'class': 'logging.StreamHandler',
    #             'formatter': 'console'
    #         },
    #         'file': {
    #             'level': 'INFO',
    #             'class': 'logging.FileHandler',
    #             'filename': os.path.join(LOGS_BASE_DIR, 'info.log'),
    #             'formatter': 'verbose',
    #         },
    #         'error': {
    #             'level': 'ERROR',
    #             'class': 'logging.FileHandler',
    #             'filename': os.path.join(LOGS_BASE_DIR, 'error.log'),
    #             'formatter': 'verbose',
    #         },
    #     },
    #     'loggers': {
    #         '': {
    #             'handlers': ['console', 'file', 'error'],
    #             'level': 'INFO',
    #             'propagate': True
    #         },
    #     },
    # }

    IS_LOCAL = True
    IS_TEST = True


class Dev(BaseConfiguration):
    DEBUG = True
    IS_LOCAL = False
    ALLOWED_HOSTS = ['*']
    SITE_URL = ''
    STATIC_ROOT = '/virtual_day/static'
    MEDIA_ROOT = '/virtual_day/media'
    SECURE_SSL_REDIRECT = False


class Prod(BaseConfiguration):
    DEBUG = False
    IS_LOCAL = False
    IS_TEST = False
    ALLOWED_HOSTS = ['*']
    SITE_URL = ''
    STATIC_ROOT = '/virtual_day/static'
    MEDIA_ROOT = '/virtual_day/media'
    SECURE_SSL_REDIRECT = True
