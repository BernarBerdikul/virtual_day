from . import codes
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, NotFound
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED, HTTP_412_PRECONDITION_FAILED, HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST)
import logging
import traceback

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """ overwrite custom exception """
    response = exception_handler(exc, context)
    logger.error(''.join(traceback.format_exception(etype=type(exc),
                                                    value=exc, tb=exc.__traceback__)))
    if response:
        errors = {}
        for field, value in response.data.items():
            if isinstance(value, list):
                errors[f'{field}'] = f'{value[0]}'
        response.data = {}
        if hasattr(exc, 'code'):
            response.data['code'] = exc.code
        else:
            if response.status_code == HTTP_401_UNAUTHORIZED:
                response.data['code'] = response.status_code
            else:
                response.data['code'] = codes.BAD_REQUEST

        if hasattr(exc, 'detail'):
            response.data['message'] = exc.detail
            response.data['errors'] = {"global": exc.detail}

        if hasattr(exc, 'redirect'):
            response.data['redirect'] = exc.redirect

        if len(errors) > 0:
            if isinstance(errors, dict):
                for key in errors:
                    response.data['message'] = ''.join(errors[key])
            else:
                response.data['message'] = errors

            response.data['errors'] = errors
    return response


class CommonException(APIException):
    detail = None
    code = None

    def __init__(self, status_code=HTTP_400_BAD_REQUEST, code=codes.BAD_REQUEST, detail='Common exception'):
        self.status_code = status_code
        self.code = code
        self.detail = detail


class NotFoundException(NotFound):
    detail = None
    code = None

    def __init__(self, status_code=HTTP_404_NOT_FOUND, code=codes.NOT_FOUND, detail='Not found exception'):
        self.status_code = status_code
        self.code = code
        self.detail = detail


class PreconditionFailedException(APIException):
    detail = None
    code = None
    redirect = None

    def __init__(self, status_code=HTTP_412_PRECONDITION_FAILED, code=codes.PRECONDITION_FAILED,
                 detail='precondition failed exception', redirect=None):
        self.status_code = status_code
        self.code = code
        self.detail = detail
        self.redirect = redirect


class ForbiddenException(APIException):
    detail = None
    code = None
    redirect = None

    def __init__(self, status_code=HTTP_403_FORBIDDEN, code=codes.FORBIDDEN, detail='forbidden', redirect=None):
        self.status_code = status_code
        self.code = code
        self.detail = detail
        self.redirect = redirect
