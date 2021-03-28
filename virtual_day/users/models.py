from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from virtual_day.mixins.models import TimestampMixin
from virtual_day.utils.image_utils import (
    avatar_path, image_push_notification_path
)
from virtual_day.utils.validators import validate_phone_number
from virtual_day.utils import constants
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """ Django Manager class for model User """
    def create_superuser(self, email, password):
        """ overwrite method for superuser creating """
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.role = constants.SUPER_ADMIN
        user.language = constants.SYSTEM_LANGUAGE
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    """ A class used to represent a User in Application """
    email = models.EmailField(
        max_length=255, null=True, blank=True, unique=True, db_index=True,
        verbose_name=_("Почта"))
    avatar = models.ImageField(
        upload_to=avatar_path, blank=True, null=True, verbose_name=_("Фото"))
    first_name = models.CharField(
        max_length=255, verbose_name=_("Имя"))
    last_name = models.CharField(
        blank=True, null=True, max_length=255, verbose_name=_("Фамилия"))
    firebase_token = models.CharField(
        blank=True, null=True, max_length=255,
        verbose_name=_("Токен firebase"))
    address = models.CharField(
        blank=True, null=True, max_length=100, verbose_name=_("Адрес"))
    role = models.PositiveSmallIntegerField(
        choices=constants.USER_TYPES, default=constants.STUDENT,
        verbose_name=_("Роль"))
    phone = models.CharField(
        max_length=13, blank=True, null=True,
        validators=[validate_phone_number], verbose_name=_("Телефон"))
    password_changed_datetime = models.DateTimeField(
        editable=False, null=True, verbose_name="Время изменения пароля")
    is_active = models.BooleanField(
        default=False, verbose_name=_("Активность"))
    language = models.CharField(
        choices=settings.LANGUAGES, max_length=32,
        default=constants.SYSTEM_LANGUAGE, verbose_name=_("Выбранный язык"))

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    @property
    def is_staff(self):
        # Anyone who is superuser can enter admin
        return self.is_superuser


class UserPushNotification(TimestampMixin):
    """ A class used to represent a Push Notifications
        to user in Application """
    title = models.CharField(
        max_length=30, blank=True,
        null=True, verbose_name=_("Название сообщения"))
    description = models.CharField(
        max_length=120, blank=True, null=True,
        verbose_name=_("Текст сообщения"))
    image = models.ImageField(
        upload_to=image_push_notification_path, blank=True, null=True,
        verbose_name=_("Фото сообщения"))
    user_ids = ArrayField(
        models.IntegerField(), blank=True, null=True,
        verbose_name=_("ID-шники пользователей"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='pushes', verbose_name=_("Пользователь"))
    response = models.JSONField(
        blank=True, null=True, max_length=1000,
        default=None, verbose_name=_("Ответ"))
    date_publication = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_("Время отправки"))
    is_sent = models.BooleanField(
        blank=True, null=True, default=False, verbose_name=_("Отправлен"))
    users_count = models.PositiveIntegerField(
        blank=True, null=True, default=0,
        verbose_name=_("Число пользователей"))
    data = models.JSONField(
        blank=True, null=True, max_length=1000, default=None,
        verbose_name=_("Данные уведомления"))

    def __str__(self):
        """ Return title when calling object """
        return f'{self.title}'

    class Meta:
        db_table = 'user_push_notification'
        verbose_name = _("Шаблон уведомления")
        verbose_name_plural = _("Шаблоны уведомления")
