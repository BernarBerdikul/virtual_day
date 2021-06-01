import phonenumbers
from virtual_day.utils import messages, constants
from virtual_day.utils.exceptions import (
    CommonException, ValidationException, notifications_wrapper
)
from uuid import UUID


def validate_phone_number(value):
    """ phone number validator """
    if len(value) != 0:
        try:
            z = phonenumbers.parse(value, None)
        except Exception:
            raise CommonException(
                detail={"phone": messages.PHONE_INCORRECT})
        if not phonenumbers.is_valid_number(z):
            raise CommonException(
                detail={"phone": messages.PHONE_INCORRECT})
    return value


def validate_password(value):
    """ validator check password's length """
    if len(value) < constants.PASSWORD_MIN_LENGTH:
        raise CommonException(
            detail={"password": messages.PASSWORD_INVALID})
    return value


def password_comparison(validated_data):
    """ comparison of passwords """
    password = validate_password(validated_data.get('password'))
    password_confirm = validate_password(validated_data.get('password_confirm'))
    if password != password_confirm:
        notifications = [notifications_wrapper(
            title=messages.PASSWORD_NOT_EQUAL,
            notice_type=constants.NOTIFY_SUCCESS)]
        raise ValidationException(notifications=notifications)
    return password


def validate_image(image, max_image_size=constants.MAX_IMAGE_SIZE,
                   field="image"):
    """ validate image size """
    if image.size > 1024 * 1024 * max_image_size:
        raise CommonException(
            detail={f"{field}": messages.MAX_IMAGE_SIZE})


def valid_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True
