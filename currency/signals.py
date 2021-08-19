import channels.layers
import json
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Currency


@receiver(post_save, sender=Currency)
def update_currency(sender, instance, **kwargs):
    group_name = 'coins'

    message = {
        'id': instance.id,
        'symbol': instance.symbol,
        'price': instance.price
    }

    channel_layers = channels.layers.get_channel_layer()

    async_to_sync(channel_layers.group_send)(
        group_name,
        {
         'type': 'user_coins',
         'event': 'New currency',
         'text': message
        }
    )
