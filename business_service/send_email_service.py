from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from virtual_day.utils import constants


def send_email(login, email, password):
    """ send email for manager with his login and congratulations"""
    message = render_to_string('send_email.html',
                               {'login': login,
                                'password': password})
    msg = EmailMessage(constants.ACTIVATION_SUBJECT, message, to=[email])
    msg.content_subtype = "html"
    msg.send()
