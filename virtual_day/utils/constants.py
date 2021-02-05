from django.utils.translation import gettext_lazy as _

REGEX_FOR_FIRST_SYMBOL = r"^[a-z]"
REGEX_FOR_LOGIN = r"^[a-zA-Z0-9_]+$"

OBJECTS_PER_PAGE_IN_ADMIN = 100
MAX_OBJECTS_IN_MODEL = 1
PASSWORD_MIN_LENGTH = 8
LOGIN_MIN_LENGTH = 5
LOGIN_MAX_LENGTH = 35

STUDENT = 0
ADMIN = 1

USER_TYPES = (
    (STUDENT, 'STUDENT'),
    (ADMIN, 'ADMIN'),
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
