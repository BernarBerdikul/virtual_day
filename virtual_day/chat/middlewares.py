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


from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class QueryAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        # Look up user from query string (you should also do things like
        # checking if it is a valid user ID, or if scope["user"] is already
        # populated).
        scope['user'] = await get_user(int(self.scope["query_string"]))

        return await self.app(scope, receive, send)


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
