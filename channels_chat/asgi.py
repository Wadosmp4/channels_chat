import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path

from currency.consumers import CoinConsumer
from chat.consumers import ChatConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [path('ws/currency/', CoinConsumer.as_asgi()),
             path('ws/<str:room_name>/', ChatConsumer.as_asgi()),]
        )
    )
})
