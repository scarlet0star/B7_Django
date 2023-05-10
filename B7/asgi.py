import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.channelsmiddleware import TokenAuthMiddleware
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'B7.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})