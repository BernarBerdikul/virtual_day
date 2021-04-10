from django.db import models
from virtual_day.users.models import User


# class Contact(models.Model):
#     user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
#     friends = models.ManyToManyField('self', blank=True)
#
#     def __str__(self):
#         return self.user.login
#
#
# class Message(models.Model):
#     contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.contact.user.login
#
#
# class Chat(models.Model):
#     participants = models.ManyToManyField(Contact, related_name='chats', blank=True)
#     messages = models.ManyToManyField(Message, blank=True)
#
#     def __str__(self):
#         return "{}".format(self.pk)
