from django.utils.translation import gettext_lazy as _
from . import constants

REQUIRED_FIELD = _("Поле обязательно для заполнения")
WRONG_REQUEST_BODY = _("Ошибочное тело запроса")
TITLE_LENGTH_MAX = _(f"Максимальная длина заголовка {constants.TITLE_LENGTH_MAX} символов")

FORBIDDEN = _("Доступ запрещен")
PASSWORD_NOT_EQUAL = _("Пароли не совпадают")
EMAIL_ALREADY_EXISTS = _("Пользователь с таким email уже существует в базе")
WRONG_LOGIN_OR_PASSWORD = _("имя или пароль введены неправильно")
PHONE_INCORRECT = _("Номер телефона введен неверно")
PASSWORD_INVALID = _(f"Пароль должен быть не менее {constants.PASSWORD_MIN_LENGTH} символов")
LOGIN_FIRST_SYMBOL_VALIDATION = _("Первый символ должен быть маленькой буквой английского алфавита, "
                                  "а логин состоять из английского алфавита, чисел и нижнего прочерка '_'")
VALUE_CONTAIN_RULE = _("Строка должна содержать только числа и буквы английского алфавита")
LOGIN_MIN_INVALID = _(f"Логин должен быть больше {constants.LOGIN_MIN_LENGTH} символов")
LOGIN_MAX_INVALID = _(f"Логин должен быть меньше {constants.LOGIN_MAX_LENGTH} символов")
