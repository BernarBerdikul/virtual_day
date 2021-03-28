import phonenumbers
from virtual_day.utils import codes, messages, constants
from virtual_day.utils.exceptions import CommonException
from uuid import UUID


def validate_phone_number(value):
    """ phone number validator """
    if len(value) != 0:
        try:
            z = phonenumbers.parse(value, None)
        except Exception:
            raise CommonException(code=codes.VALIDATION_ERROR,
                                  detail=messages.PHONE_INCORRECT)
        if not phonenumbers.is_valid_number(z):
            raise CommonException(code=codes.VALIDATION_ERROR,
                                  detail=messages.PHONE_INCORRECT)
    return value


def validate_password(value):
    """ validator check password's length """
    if len(value) < constants.PASSWORD_MIN_LENGTH:
        raise CommonException(code=codes.VALIDATION_ERROR,
                              detail=messages.PASSWORD_INVALID)
    return value


def password_comparison(validated_data):
    """ comparison of passwords """
    password = validate_password(validated_data.get('password'))
    password_confirm = validate_password(validated_data.get('password_confirm'))
    if password != password_confirm:
        raise CommonException(code=codes.VALIDATION_ERROR,
                              detail=messages.PASSWORD_NOT_EQUAL)
    return password


def validate_image(image, max_image_size=constants.MAX_IMAGE_SIZE,
                   field="image"):
    """ validate image size """
    if image.size > 1024 * 1024 * max_image_size:
        raise CommonException(
            code=codes.VALIDATION_ERROR,
            detail={f"{field}": messages.MAX_IMAGE_SIZE})


def valid_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True
