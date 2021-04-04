from django.db import models
from django.utils.safestring import mark_safe
from virtual_day.mixins.models import TimestampMixin, ValidateErrorMixin
from virtual_day.utils.image_utils import (
    billboard_image_path, pdf_file_image_path
)
from django.utils.translation import gettext_lazy as _
from virtual_day.utils import constants
from translations.models import Translatable


class PDFForBillboard(TimestampMixin, ValidateErrorMixin):
    pdf_file = models.FileField(
        upload_to=pdf_file_image_path, blank=True, null=True,
        verbose_name=_("Презентация"))
    language = models.CharField(
        max_length=2,
        choices=constants.TRANSLATION_LANGUAGES,
        verbose_name=_("язык перевода"))

    def __str__(self):
        """ Return language and pdf_file when calling object """
        return f'{self.language} - {self.pdf_file}'

    class Meta:
        db_table = 'pdf_billboard'
        verbose_name = _("Билборд")
        verbose_name_plural = _("Билборды")


class URLForBillboard(TimestampMixin, ValidateErrorMixin):
    url_link = models.CharField(
        max_length=500, null=True, blank=True,
        verbose_name=_("Ссылка на видео"))
    language = models.CharField(
        max_length=2,
        choices=constants.TRANSLATION_LANGUAGES,
        verbose_name=_("язык перевода"))

    def __str__(self):
        """ Return language and url_link when calling object """
        return f'{self.language} - {self.url_link}'

    class Meta:
        db_table = 'url_billboard'
        verbose_name = _("Билборд")
        verbose_name_plural = _("Билборды")


class Billboard(Translatable, TimestampMixin, ValidateErrorMixin):
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
    is_static = models.BooleanField(
        default=True, verbose_name=_("Статичный"))
    unique_key = models.PositiveSmallIntegerField(
        choices=constants.UNIQUE_KEY_FOR_BILLBOARD, blank=True, null=True,
        verbose_name=_("ключ"))
    pdf_file = models.ForeignKey(
        PDFForBillboard, blank=True, null=True, on_delete=models.CASCADE,
        verbose_name=_("Презентация"))
    url_link = models.ForeignKey(
        URLForBillboard, null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=_("Ссылка на видео"))

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


class Schedule(Translatable, TimestampMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    period_start = models.PositiveIntegerField(
        verbose_name=_("Время начала показа"))
    period_end = models.PositiveIntegerField(
        verbose_name=_("Время конца показа"))
    event = models.CharField(
        blank=True, null=True, max_length=constants.EVENT_LENGTH_MAX,
        verbose_name=_("Событие"))
    billboard = models.ForeignKey(
        Billboard, on_delete=models.CASCADE, related_name='schedules',
        blank=True, null=True, verbose_name=_("Билборд"))
    speaker_id = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_("ID спикера"))

    def __str__(self):
        """ Return period_start, period_end and event when calling object """
        return f'{self.period_start} - {self.period_end} - {self.event}'

    class Meta:
        db_table = 'schedule'
        verbose_name = _("Расписание")
        verbose_name_plural = _("Расписание")

    class TranslatableMeta:
        """ field that is translated in the database """
        fields = ['event']
