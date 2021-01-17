import phonenumbers
from virtual_day.utils import codes, messages, constants
from virtual_day.utils.exceptions import CommonException
from uuid import UUID
import re


def validate_phone_number(value):
    try:
        z = phonenumbers.parse(value, None)
    except:
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.PHONE_INCORRECT)
    if not phonenumbers.is_valid_number(z):
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.PHONE_INCORRECT)


def validate_password(value):
    if len(value) < constants.PASSWORD_MIN_LENGTH:
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.PASSOWRD_INVALID)
    return value


def validate_login(value):
    if not re.match(constants.REGEX_FOR_FIRST_SYMBOL, value):
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.FIRST_SYMBOL_VALIDATION)
    if not re.match(constants.REGEX_FOR_LOGIN, value):
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.VALUE_CONTAIN_RULE)
    if len(value) < constants.LOGIN_MIN_LENGTH:
        raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.LOGIN_INVALID)
    return value


def valid_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True
