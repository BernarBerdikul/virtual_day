from django.utils.translation import gettext_lazy as _
from . import constants

REQUIRED_FIELD = _("Поле обязательно для заполнения")
# WRONG_REQUEST_BODY_PDF = \
#     _("Ошибочное тело запроса, требуется файл с презентацией")
# WRONG_REQUEST_BODY_LINK = \
#     _("Ошибочное тело запроса, требуется ссылка на видео")
TITLE_LENGTH_MAX = \
    _(f"Максимальная длина заголовка {constants.TITLE_LENGTH_MAX} символов")
EVENT_LENGTH_MAX = \
    _(f"Максимальная длина события {constants.EVENT_LENGTH_MAX} символов")

FORBIDDEN = _("Доступ запрещен")
PASSWORD_NOT_EQUAL = _("Пароли не совпадают")
EMAIL_ALREADY_EXISTS = _("Пользователь с таким email уже существует в базе")
WRONG_EMAIL_OR_PASSWORD = _("почта или пароль введены неправильно")
SECRET_KEY_NOT_FOUND = _("Не найден секретый ключ")
PHONE_INCORRECT = _("Номер телефона введен неверно")
PASSWORD_INVALID = \
    _(f"Пароль должен быть не менее {constants.PASSWORD_MIN_LENGTH} символов")
LOGIN_FIRST_SYMBOL_VALIDATION = \
    _("Первый символ должен быть маленькой буквой английского алфавита, "
      "а логин состоять из английского алфавита, чисел и нижнего прочерка '_'")
VALUE_CONTAIN_RULE = \
    _("Строка должна содержать только числа и буквы английского алфавита")
LOGIN_MIN_INVALID = \
    _(f"Логин должен быть больше {constants.LOGIN_MIN_LENGTH} символов")
LOGIN_MAX_INVALID = \
    _(f"Логин должен быть меньше {constants.LOGIN_MAX_LENGTH} символов")
MAX_IMAGE_SIZE = _(f"Максимально допустимый размер изображения - "
                   f"{constants.MAX_IMAGE_SIZE} мб")
RESTAURANT_PUSH_ALREADY_SENT = \
    _("Уведомление уже было отправлено и его нельзя изменить")
PUSH_LIMIT_MESSAGE = _("Вы можете отправить только одно уведомление в день!")
