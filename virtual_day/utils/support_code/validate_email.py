from django.utils.regex_helper import _lazy_re_compile
import re

"""
CODE from lib python 'validators',
link: https://github.com/kvesteri/validators/blob/master/validators/email.py
This code base on 'Django' email validator
Need to catch custom exception and return wrong message to front
"""

user_regex = _lazy_re_compile(
    # dot-atom
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"
    # quoted-string
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]'
    r'|\\[\001-\011\013\014\016-\177])*"\Z)',
    re.IGNORECASE)
domain_regex = _lazy_re_compile(
    # max length for domain name labels is 63 characters per RFC 1034
    r'((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z',
    re.IGNORECASE)
domain_whitelist = ['localhost']


def email(value, whitelist=None):
    """
    Validate an email address.
    """
    if whitelist is None:
        whitelist = domain_whitelist

    if not value or '@' not in value:
        return False

    user_part, domain_part = value.rsplit('@', 1)

    if not user_regex.match(user_part):
        return False

    if len(user_part.encode("utf-8")) > 64:
        return False

    if domain_part not in whitelist and not domain_regex.match(domain_part):
        # Try for possible IDN domain-part
        try:
            domain_part = domain_part.encode('idna').decode('ascii')
            return domain_regex.match(domain_part)
        except UnicodeError:
            return False
    return True
