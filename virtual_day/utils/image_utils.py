import os
from urllib.parse import urljoin
import time
from django.conf import settings


def get_full_url(image):
    """
    params: image - instance of ImageField
    """
    if not image:
        return None
    return urljoin(settings.SITE_URL, image.url)


def __files_unique_path(instance, filename, folder_name='images'):
    # file will be uploaded to MEDIA_ROOT/<folder_name>/<filename>
    _, ext = os.path.splitext(filename)
    return f"{instance}/{folder_name}{ext}"


def image_logo_path(instance, filename):
    return __files_unique_path(instance.id, filename, folder_name=f'image_logo_{round(time.time())}')


def image_bg_path(instance, filename):
    return __files_unique_path(instance.id, filename, folder_name=f'image_bg_{round(time.time())}')


def image_panorama_path(instance, filename):
    return __files_unique_path(instance.id, filename, folder_name=f'image_panorama_{round(time.time())}')


def qr_codes_path(instance, filename):
    return __files_unique_path(instance.id, filename, folder_name=f'qr_code_{round(time.time())}')


def image_dish_path(instance, filename):
    return __files_unique_path(instance.menu.restaurant.id, filename, folder_name=f'dish/{instance.id}_{round(time.time())}')


def image_restaurant_news_path(instance, filename):
    return __files_unique_path(instance.restaurant.id, filename, folder_name=f'news/{instance.id}_{round(time.time())}')


def image_waiter_path(instance, filename):
    return __files_unique_path(instance.restaurant.id, filename, folder_name=f'waiter/{instance.id}_{round(time.time())}')


def image_user_features_path(instance, filename):
    return __files_unique_path(instance, filename, folder_name=f'user_features/feature_{instance.id}_{round(time.time())}')


def image_push_notification_path(instance, filename):
    return __files_unique_path(instance.restaurant.id, filename, folder_name=f'push_notification/{instance.id}_{round(time.time())}')


def image_dish_adds_path(instance, filename):
    return __files_unique_path(instance, filename, folder_name=f'image_dish_adds/{instance.id}_{round(time.time())}')


def image_user_path(instance, filename):
    return __files_unique_path(instance, filename, folder_name=f'user/{instance.id}_{round(time.time())}')


def image_market_item(instance, filename):
    return __files_unique_path(instance, filename, folder_name=f'market/image_{instance.id}_{round(time.time())}')


def file_model_market_item(instance, filename):
    return __files_unique_path(instance, filename, folder_name=f'market/model3d_{instance.id}_{round(time.time())}')
