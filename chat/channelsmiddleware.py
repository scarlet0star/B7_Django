from django.contrib.auth.models import AnonymousUser

from rest_framework_simplejwt.tokens import AccessToken
from users.models import User
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(token_key):
    try:
        access_token = AccessToken(token_key)
        user_id = access_token.get('user_id', None)

    except user_id is None:
        return AnonymousUser()

    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)

        except ValueError:
            token_key = None
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)

        return await super().__call__(scope, receive, send)