from . import constants
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, NotFound
from rest_framework.status import (
    HTTP_412_PRECONDITION_FAILED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
import logging
import traceback

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """ overwrite custom exception """
    logger.error(''.join(traceback.format_exception(
        etype=type(exc), value=exc, tb=exc.__traceback__)))
    response = exception_handler(exc, context)
    if response:
        errors = {}
        for field, value in response.data.items():
            if isinstance(value, list):
                errors[f'{field}'] = f'{value[0]}'
        response.data = {"success": False}
        if hasattr(exc, 'detail'):
            response.data['errors'] = exc.detail
        if hasattr(exc, 'redirect'):
            response.data['redirect'] = exc.redirect
        if hasattr(exc, 'notifications'):
            response.data['notifications'] = exc.notifications
    return response


def notifications_wrapper(title, notice_type: int, description=None) -> dict:
    return {"title": title,
            "description": description,
            "type": constants.NOTIFY_TYPES[notice_type][1]}


class ValidationException(APIException):
    status_code = HTTP_200_OK

    def __init__(self, detail={}, notifications=None):
        self.detail = detail
        self.notifications = notifications


class CommonException(APIException):

    def __init__(self, status_code=HTTP_400_BAD_REQUEST,
                 detail={}, notifications=None):
        self.status_code = status_code
        self.detail = detail
        self.notifications = notifications


class NotFoundException(NotFound):
    status_code = HTTP_404_NOT_FOUND

    def __init__(self, detail={}, notifications=None):
        self.detail = detail
        self.notifications = notifications


class PreconditionFailedException(APIException):
    status_code = HTTP_412_PRECONDITION_FAILED

    def __init__(self, detail={}, redirect=None, notifications=None):
        self.detail = detail
        self.redirect = redirect
        self.notifications = notifications


class ForbiddenException(APIException):
    status_code = HTTP_403_FORBIDDEN,

    def __init__(self, detail={}, redirect=None, notifications=None):
        self.detail = detail
        self.redirect = redirect
        self.notifications = notifications
