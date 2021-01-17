from django.utils.translation import gettext_lazy as _

OBJECTS_PER_PAGE_IN_ADMIN = 100
MAX_OBJECTS_IN_MODEL = 1
PASSWORD_MIN_LENGTH = 8
LOGIN_MIN_LENGTH = 5
TAG_MIN_LENGTH = 3
RESTAURANT_DESCRIPTION_MIN_LENGTH = 120
REASON_FOR_CHANGE_MIN_LENGTH = 4
TITLE_MIN_LENGTH = 1
LENGTH_OF_TOKEN = 20

ADMIN = 'ADMIN'
MANAGER = 'MANAGER'

USER_TYPES = (
    (MANAGER, _("Менеджер")),
    (ADMIN, _("Админ")),
)

ORDER_PAY_TYPES = (
    (0, _("Наличными")),
    (1, _("Безналичными")),
)

MARKET_PAY_TYPES = (
    (0, _("Счет фактура")),
    (1, _("Карта")),
)

SEX_TYPE = (
    ('MEN', _("Мужской")),
    ('WOMEN', _("Женский")),
)

PUBLISHED = 'PUBLISHED'
UNPUBLISHED = 'UNPUBLISHED'

PUBLISHED_STATUS = (
    (PUBLISHED, _("Опубликовано")),
    (UNPUBLISHED, _("Не опубликовано")),
)

YES = 'YES'
NO = 'NO'

DELIVERY_ACCESS = (
    (YES, _("Да")),
    (NO, _("Нет")),
)

BASKET_TYPES = (
    (1, _("Заказ в заведении")),
    (2, _("Доставка")),
    (3, _("Самовывоз")),
)

DAYS_OF_THE_WEEK = (
    (1, _("ПН")),
    (2, _("ВТ")),
    (3, _("СР")),
    (4, _("ЧТ")),
    (5, _("ПТ")),
    (6, _("СБ")),
    (7, _("ВС")),
)

TIMETABLE_STATUS = (
    (1, _("Выбрать время")),
    (2, _("Круглосуточно")),
    (3, _("Выходной")),
)

PLATFORM_TYPES = (
    (1, _("Desktop")),
    (2, _("Android")),
    (3, _("IOS")),
)

MENU_TYPES = (
    (1, _("Меню доставки")),
    (2, _("Меню основное")),
    (3, _("Меню барное")),
    (4, _("Завтраки")),
    (5, _("Меню напитков")),
    (6, _("Меню торжеств")),
    (7, _("Меню на вынос")),
    (8, _("Меню детское")),
    (9, _("Меню от шефа")),
    (10, _("Комплексные обеды")),
    (11, _("Эксклюзивное меню")),
    (12, _("Премиальное меню")),
)

SUBMENU_TYPES = (
    (1, _("Гарниры")),
    (2, _("Десерты")),
    (3, _("Холодные закуски")),
    (4, _("Горячие закуски")),
    (5, _("Салаты")),
    (6, _("Первые блюда")),
    (7, _("Вторые блюда")),
    (8, _("Шашлыки")),
    (9, _("Бургеры")),
    (10, _("Паста")),
    (11, _("Пицца")),
    (12, _("Выпечка")),
    (13, _("Завтраки")),
    (14, _("Сеты")),
    (15, _("Закуски")),
    (16, _("Напитки")),
)


MARKET_ORDER_STATUS = (
    (0, _("Новый")),
    (1, _("В обработке")),
    (2, _("Отправлен")),
    (3, _("Завершен")),
    (4, _("Неудача")),
)

STATUS_CODE_NULL = 0
STATUS_CODE_AWAITING = 1
STATUS_CODE_AUTHORIZED = 2
STATUS_CODE_COMPLETED = 3
STATUS_CODE_CANCELLED = 4
STATUS_CODE_DECLINED = 5

MARKET_ORDER_PAY_STATUS = (
    (STATUS_CODE_NULL, None),
    (STATUS_CODE_AWAITING, _("Ожидает аутентификации")),
    (STATUS_CODE_AUTHORIZED, _("Авторизована")),
    (STATUS_CODE_COMPLETED, _("Завершена")),
    (STATUS_CODE_CANCELLED, _("Отменена")),
    (STATUS_CODE_DECLINED, _("Отклонено")),
)

CANCELED = 'CANCELED'
CREATED = 'CREATED'
SCANNED = 'SCANNED'
ACCEPTED = 'ACCEPTED'
DONE = 'DONE'

ORDER_STATUS = (
    (CANCELED, _("Отменен")),
    (CREATED, _("Создан")),
    (SCANNED, _("Отсканирован официантом")),
    (ACCEPTED, _("Принят")),
    (DONE, _("Завершен")),
)

VALIDATION_REQUEST_TYPE = (
    (1, _("Phone")),
    (2, _("Instagram")),
)

TELEPHONE_TYPE = (
    (1, _("Телефон основной")),
    (2, _("Телефон администрации")),
    (3, _("Телефон доставки")),
    (4, _("Телефон предзаказа")),
)

MESSENGER_TYPE = (
    (1, "WhatsApp"),
    (2, "Viber"),
    (3, "Telegram"),
    (4, "Skype"),
    (5, "Facebook Messenger"),
    (6, "Hangouts Google"),
    (7, "Google Talk"),
    (8, "Mail.Ru Агент"),
    (9, "Snapchat"),
)

JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

MONTHS = (
    (JANUARY, _('янв'), _('январь')),
    (FEBRUARY, _('фев'), _('февраль')),
    (MARCH, _('мар'), _('март')),
    (APRIL, _('апр'), _('апрель')),
    (MAY, _('май'), _('май')),
    (JUNE, _('июнь'), _('июнь')),
    (JULY, _('июль'), _('июль')),
    (AUGUST, _('авг'), _('август')),
    (SEPTEMBER, _('сен'), _('сентябрь')),
    (OCTOBER, _('окт'), _('октябрь')),
    (NOVEMBER, _('ноя'), _('ноябрь')),
    (DECEMBER, _('дек'), _('декабрь')),
)


QR_CODE_IMAGE_SIZE = (400, 400)
ACTIVATION_SUBJECT = "Активация аккаунта"
REDIRECT_LOGIN_LINK = "login"
REDIRECT_RESTAURANT_LINK = "manage_manager"
REDIRECT_VALIDATE_LINK = "validate"

REGEX_FOR_FIRST_SYMBOL = r"^[a-z]"
REGEX_FOR_TAG = r"^[a-zA-Z0-9_]+$"
REGEX_FOR_LOGIN = r"^[a-zA-Z0-9_]+$"

# Bitrix24 methods
CALL_LEAD_ADD = 'crm.lead.add'
CALL_DEAL_ADD = 'crm.deal.add'
CALL_DEAL_LIST = 'crm.deal.list'

MINIMAL_QUANTITY = 3
PRICE_LIST_HARD = 2.263157894736842
PRICE_LIST_NORMAL = 1.539473684210526
PRICE_LIST_EASY = 1.203947368421053

CLOUD_PAYMENTS_LOGIN = 'pk_a36ee02a4b0c3049c27125988c333'
CLOUD_PAYMENTS_PASSWORD = 'ee9c387bf1f14e69a6828b26bdc77b8e'
