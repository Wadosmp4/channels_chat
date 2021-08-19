from channels.generic.websocket import AsyncJsonWebsocketConsumer


class CoinConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.group_name = 'coins'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def user_coins(self, event):
        print(f"Got message {event} at {self.channel_name}")
        await self.send_json(event)
