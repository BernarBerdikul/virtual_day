from urllib.parse import urlparse, parse_qs
from channels.auth import AuthMiddlewareStack
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

from asgiref.sync import sync_to_async
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model

User = get_user_model()


class TokenAuthMiddleware:
    
    def __init__(self, inner):
        self.inner = inner    

    def __call__(self, scope):
        query_string = scope['query_string']
        if query_string:
            try:
                parsed_query = parse_qs(query_string)
                token_key = parsed_query[b'token'][0].decode()
                token_name = 'token'
                if token_name == 'token':
                    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                    payload = jwt_decode_handler(token_key)
                    scope['user_id'] = payload['user_id']
                    close_old_connections()
            except AuthenticationFailed:
                scope['user'] = AnonymousUser()
        else:
            scope['user'] = AnonymousUser()
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))
