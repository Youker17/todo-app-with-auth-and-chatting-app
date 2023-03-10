"""
ASGI config for todo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatting.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')



application = ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        "websocket":AuthMiddlewareStack(
        URLRouter(
            chatting.routing.websocket_urlpatterns
        ))
    }
    )
