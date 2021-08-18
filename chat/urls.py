from django.urls import path

from .views import ChatView
from .views import ChatRoomView


urlpatterns = [
    path('', ChatView.as_view(), name='index'),
    path('<str:room_name>/', ChatRoomView.as_view(), name='room'),
]
