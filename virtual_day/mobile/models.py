from django.db import models
from virtual_day.mixins.models import TimestampMixin
from virtual_day.users.models import User


class Chat(TimestampMixin):
    # team = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="chats", default=None)
    users = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return "{}".format(self.pk)

    def get_last_10_messages(self, offset=0, limit=10):
        if offset == 0:
            return self.messages.all().order_by('-created_at')[:limit]
        return self.messages.filter(pk__lt=offset).order_by('-created_at')[:limit]


class Message(TimestampMixin):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    data = models.JSONField(max_length=1000, blank=True, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return self.user.login
