from django.urls import path

from .views import ChatView
from .views import ChatRoomView
from .views import index
from .views import video_feed
from .views import webcam_feed



urlpatterns = [
    path('', ChatView.as_view(), name='currency'),
    path('<str:room_name>/', ChatRoomView.as_view(), name='room'),
]
