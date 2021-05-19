from django.db import models
from django.utils.safestring import mark_safe
from virtual_day.mixins.models import DateTimeMixin, ValidateErrorMixin
from virtual_day.utils.image_utils import (
    billboard_image_path, pdf_file_image_path
)
from django.utils.translation import gettext_lazy as _
from virtual_day.utils import constants
from translations.models import Translatable


class DodDay(Translatable, DateTimeMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    day_date = models.DateField(verbose_name=_("Дата дня"))
    enable = models.BooleanField(
        default=True, verbose_name=_("Активен"))

    def __str__(self):
        """ Return period_start, period_end and event when calling object """
        return f'{self.day_date}'

    class Meta:
        db_table = 'dod_day'
        verbose_name = _("День ДОДа")
        verbose_name_plural = _("Дни ДОДа")


class Event(Translatable, DateTimeMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    period_start = models.TimeField(
        verbose_name=_("Время начала показа"))
    period_end = models.TimeField(
        verbose_name=_("Время конца показа"))
    title = models.CharField(
        blank=True, null=True, max_length=constants.EVENT_LENGTH_MAX,
        verbose_name=_("Название события"))
    dod_day = models.ForeignKey(
        DodDay, on_delete=models.CASCADE, verbose_name=_("День ДОДа"))
    event_type = models.PositiveSmallIntegerField(
        choices=constants.EVENT_TYPE, verbose_name=_("Тип события"))
    enable = models.BooleanField(
        default=True, verbose_name=_("Активен"))

    def __str__(self):
        """ Return period_start, period_end and event when calling object """
        return f'{self.period_start} - {self.period_end} - {self.event}'

    class Meta:
        db_table = 'event'
        verbose_name = _("Событие")
        verbose_name_plural = _("События")

    class TranslatableMeta:
        """ field that is translated in the database """
        fields = ['title']


class Billboard(Translatable, DateTimeMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    title = models.CharField(
        blank=True, null=True, max_length=constants.TITLE_LENGTH_MAX,
        verbose_name=_("Заголовок билборда"))
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Текст билборда"))
    image = models.ImageField(
        upload_to=billboard_image_path, blank=True, null=True,
        verbose_name=_("Фото"))
    type = models.PositiveSmallIntegerField(
        choices=constants.BILLBOARD_TYPES, default=constants.TEXT,
        verbose_name=_("Тип билборда"))
    enable = models.BooleanField(
        default=True, verbose_name=_("Активен"))
    event = models.ForeignKey(
        Event, on_delete=models.PROTECT, verbose_name=_("Событие"))
    is_static = models.BooleanField(
        default=True, verbose_name=_("Статичный"))
    unique_key = models.PositiveSmallIntegerField(
        choices=constants.UNIQUE_KEY_FOR_BILLBOARD, blank=True, null=True,
        verbose_name=_("ключ"))

    def billboard_image(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="160px" height="120px" />')

    def __str__(self):
        """ Return billboard title and enable status when calling object """
        return f'{self.title} - {self.enable}'

    class Meta:
        db_table = 'billboard'
        verbose_name = _("Билборд")
        verbose_name_plural = _("Билборды")

    class TranslatableMeta:
        """ field that is translated in the database """
        fields = ['title', 'description']


class MediaBillboard(DateTimeMixin, ValidateErrorMixin):
    billboard = models.ForeignKey(
        Billboard, on_delete=models.CASCADE,
        related_name='billboard_statics', verbose_name=_("Билборд"))
    pdf_file = models.FileField(
        upload_to=pdf_file_image_path, blank=True, null=True,
        verbose_name=_("Презентация"))
    url_link = models.CharField(
        max_length=500, null=True, blank=True,
        verbose_name=_("Ссылка на видео"))
    language = models.CharField(
        max_length=2,
        choices=constants.TRANSLATION_LANGUAGES,
        verbose_name=_("язык перевода"))

    def __str__(self):
        """ Return billboard and language when calling object """
        return f'{self.billboard} - {self.language}'

    class Meta:
        db_table = 'media_billboard'
        verbose_name = _("Статика билборда")
        verbose_name_plural = _("Статика билбордов")


class Lecture(Translatable, DateTimeMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    class_room = models.PositiveSmallIntegerField(
        choices=constants.CLASS_ROOM, verbose_name=_("Дата дня"))
    speaker = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name=_("Спикер"))
    event = models.OneToOneField(
        Event, on_delete=models.PROTECT, related_name='lecture',
        verbose_name=_("Событие"))
    enable = models.BooleanField(
        default=True, verbose_name=_("Активен"))

    def __str__(self):
        """ Return class_room when calling object """
        return f'{self.class_room}'

    class Meta:
        db_table = 'lecture'
        verbose_name = _("Лекция")
        verbose_name_plural = _("Лекции")
