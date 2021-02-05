import os
from urllib.parse import urljoin
from django.conf import settings
import uuid


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
    return f"{folder_name}/{uuid.uuid4()}{ext}"


def avatar_path(instance, filename):
    return __files_unique_path(instance, filename, folder_name='avatars')

