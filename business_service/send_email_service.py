from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from virtual_day.utils import constants


def send_email(name: str, email: str, password: str):
    """ send email for manager with his name and password"""
    message = render_to_string('send_email.html',
                               {'name': name,
                                'password': password})
    msg = EmailMessage(constants.ACTIVATION_SUBJECT, message, to=[email])
    msg.content_subtype = "html"
    msg.send()
