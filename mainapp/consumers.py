from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected .....", event)
        async_to_sync (self.channel_layer.group_add)(
            "programmers", self.channel_name
        )
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self, event):
        print("receiving riad.....", event['text'])
        async_to_sync (self.channel_layer.group_send)(
            'programmers', 
            {
                'type':'chat.message',
                'message': event['text']
            }
        )
    def chat_message(self, event):
        print("Event 55 .. ",event)
        print('Actual Data .. ', event['message'])
        self.send({
            'type':'websocket.send',
            'text': event['message'],
        })

    def websocket_disconnect(self, event):
        print("Channel Layer ..", self.channel_layer)

        print("Channel Name ..", self.channel_name)

        async_to_sync (self.channel_layer.group_discard)(
            "programmers", self.channel_name
        )

        print("disconnected .....", event)
        raise StopConsumer()

