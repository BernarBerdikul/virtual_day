import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model

from virtual_day.users.models import User
from virtual_day.utils.chat_util import message_to_json
from .models import Message, Chat

User = get_user_model()

import logging

logger = logging.getLogger(__name__)


class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        try:
            chat = Chat.objects.all().first()
            limit = data['limit']
            offset = data['offset']
            content = {
                'command': 'messages',
                'messages': self.messages_to_json(chat.get_last_10_messages(offset=offset, limit=limit))
            }
            self.send_message(content)
        except Exception as e:
            logger.error(str(e))

    def new_message(self, data):
        chat = Chat.objects.all().first()
        message = Message.objects.create(
            student=self.user,
            content=data['message'],
            chat_id=chat.id)
        content = {
            'command': 'new_message',
            'message': message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            if message.data:
                logger.info(message.data)
            result.append(message_to_json(message))
        return result[::-1]

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        try:
            # Get authorized user
            self.user = User.objects.get(id=self.scope["user_id"])
            logger.info(str(self.user))

            # User should be student, get information about student
            self.student = Student.objects.get(user=self.user)
            logger.info(str(self.student))

            # Room name equal to team ID 
            self.room_name = self.scope['url_route']['kwargs']['room_name']

            self.room_group_name = 'chat_%s' % self.room_name
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
        except Exception as e:
            logger.error(str(e))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        logger.info(str(text_data))
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
