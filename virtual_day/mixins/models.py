from django.db import models


class TimestampMixin(models.Model):
    """
    A class used to represent an TimestampMixin
    ...
    Fields
    ----------
    created_at: datetime
        date and time when object is created
    updated_at: datetime
        date and time when object was updated
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Время последнего изменения')

    class Meta:
        abstract = True
