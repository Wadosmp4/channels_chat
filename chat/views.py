from django.views import View
from django.shortcuts import render
from .models import Message


class ChatView(View):
    greeting = "Good grief"

    def get(self, request):
        return render(request, 'chat/index.html')


class ChatRoomView(View):

    def get(self, request, room_name):
        username = request.GET.get('username')
        if not username:
            username = 'Baban'

        messages = Message.objects.filter(room=room_name)[0:25]

        return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
