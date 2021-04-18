from django.utils.translation import gettext_lazy as _

GOOGLE_APPLICATION_CREDENTIALS = \
    r'D:\PycharmProjects\virtual_day\virtual_day\firebase\ServiceAccount.json'

TRANSLATION_LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
    ('kk', _('Kazakh')),
    ('de', _('German')),
)

OBJECTS_PER_PAGE_IN_ADMIN = 100
MAX_OBJECTS_IN_MODEL = 1
PASSWORD_MIN_LENGTH = 8
LOGIN_MIN_LENGTH = 5
LOGIN_MAX_LENGTH = 35
MAX_IMAGE_SIZE = 20  # in Mb

SUPER_ADMIN = 0
ADMIN = 1
MODERATOR = 2
SPEAKER = 3
STUDENT = 4

USER_TYPES = (
    (SUPER_ADMIN, 'SUPER_ADMIN'),
    (ADMIN, 'ADMIN'),
    (MODERATOR, 'MODERATOR'),
    (SPEAKER, 'SPEAKER'),
    (STUDENT, 'STUDENT'),
)

SYSTEM_LANGUAGE = "ru"

DAYS_OF_THE_WEEK = (
    (1, _("ПН")),
    (2, _("ВТ")),
    (3, _("СР")),
    (4, _("ЧТ")),
    (5, _("ПТ")),
    (6, _("СБ")),
    (7, _("ВС")),
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

ACTIVATION_SUBJECT = "Активация аккаунта"

###############################################################################
""" MOBILE APP """
VIDEO = 0
TEXT = 1

BILLBOARD_TYPES = (
    (VIDEO, 'VIDEO'),
    (TEXT, 'PDF'),
)

MAJOR1 = 1
MAJOR2 = 2
MAJOR3 = 3
MAJOR4 = 4
MAJOR5 = 5
MAJOR6 = 6
MAJOR7 = 7

CLASS_ROOM = (
    (0, _("Аудитория 1")),
    (1, _("Аудитория 2")),
    (2, _("Аудитория 3")),
    (3, _("Аудитория 4")),
    (4, _("Аудитория 5")),
    (5, _("Аудитория 6")),
    (6, _("Аудитория 7")),
)

TYPE_LECTURE = 0
TYPE_BILLBOARD = 1

EVENT_TYPE = (
    (TYPE_LECTURE, _("Лекция")),
    (TYPE_BILLBOARD, _("Билборд")),
)

UNIQUE_KEY_FOR_BILLBOARD = (
    (MAJOR1, _("Информационные системы")),
    (MAJOR2, _("Логистика")),
    (MAJOR3, _("Энергетика")),
    (MAJOR4, _("Финансы")),
    (MAJOR5, _("Маркетинг")),
    (MAJOR6, _("Менеджмент")),
    (MAJOR7, _("Международные отношения")),
)

""" BILLBOARD """
TITLE_LENGTH_MAX = 50
EVENT_LENGTH_MAX = 255
