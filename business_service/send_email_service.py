from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from virtual_day.utils import constants


async def send_email(login: str, email: str, password: str):
    """ send email for manager with his login and congratulations"""
    message = render_to_string('send_email.html',
                               {'login': login,
                                'password': password})
    msg = EmailMessage(constants.ACTIVATION_SUBJECT, message, to=[email])
    msg.content_subtype = "html"
    msg.send()


async def send_for_admin_email(email: str, secret_key: str):
    """ send email for admin with secret_key """
    message = render_to_string(
        'send_for_admin_email.html',
        {'secret_key': secret_key})
    msg = EmailMessage(constants.ACTIVATION_SUBJECT, message, to=[email])
    msg.content_subtype = "html"
    msg.send()
