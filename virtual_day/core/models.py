from django.db import models
from django.utils.safestring import mark_safe
from virtual_day.mixins.models import TimestampMixin, ValidateErrorMixin
from virtual_day.utils.image_utils import billboard_image_path
from django.utils.translation import gettext_lazy as _
from virtual_day.utils import constants


class Billboard(TimestampMixin, ValidateErrorMixin):
    """ A class used to represent an Billboard in application """
    title = models.CharField(max_length=255, verbose_name=_("Заголовок билборда"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Текст билборда"))
    url_link = models.CharField(max_length=500, null=True, blank=True, verbose_name=_("Ссылка на видео"))
    image = models.ImageField(upload_to=billboard_image_path, blank=True, null=True, verbose_name=_("Фото"))
    type = models.PositiveSmallIntegerField(choices=constants.COURSE_TYPES, default=constants.TEXT,
                                            verbose_name=_("Тип билборда"))
    enable = models.BooleanField(default=True, verbose_name=_("Активен"))
    period_start = models.TimeField(verbose_name=_("Время начала показа"))
    period_end = models.TimeField(verbose_name=_("Время конца показа"))

    def billboard_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="160px" height="120px" />')

    def __str__(self):
        """ Return billboard title and enable status when calling object """
        return f'{self.title} - {self.enable}'

    class Meta:
        db_table = 'billboard'
        verbose_name = _("Билборд")
        verbose_name_plural = _("Билборды")
