import logging

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from jwt import decode as jwt_decode
from jwt import exceptions as jwt_exceptions
from rest_framework_simplejwt.tokens import UntypedToken

logger = logging.getLogger(__name__)


@database_sync_to_async
def get_user(token):
    try:
        UntypedToken(token)
        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_data.get("user_id")
        from django.contrib.auth import get_user_model

        User = get_user_model()
        user = User.objects.get(id=user_id)
        return user
    except jwt_exceptions.InvalidTokenError as e:
        logger.debug(f"Invalid token: {e}")
        return AnonymousUser()
    except Exception as e:
        logger.exception("Unexpected error during token validation.")
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        token = None

        query_string = scope["query_string"].decode()
        query_params = dict(
            qc.split("=") for qc in query_string.split("&") if "=" in qc
        )
        token = query_params.get("token", None)

        if token is None:
            headers = dict(scope["headers"])
            if b"authorization" in headers:
                auth_header = headers[b"authorization"].decode()
                if auth_header.startswith("Bearer "):
                    token = auth_header[7:]

        if token:
            user = await get_user(token)
            scope["user"] = user
        else:
            scope["user"] = AnonymousUser()
        return await super().__call__(scope, receive, send)
