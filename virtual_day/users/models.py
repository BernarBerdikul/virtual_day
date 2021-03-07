from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from virtual_day.mixins.models import TimestampMixin
from virtual_day.utils.image_utils import avatar_path
from virtual_day.utils.validators import validate_phone_number
from virtual_day.utils import constants
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """ Django Manager class for model User """
    def create_superuser(self, login, password):
        """ overwrite method for superuser creating """
        user = self.model(login=login)
        user.set_password(password)
        user.is_superuser = True
        user.role = constants.ADMIN
        user.language = 'ru'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    """ A class used to represent a User in Application """
    login = models.CharField(max_length=255, unique=True, verbose_name=_("Логин"))
    avatar = models.ImageField(upload_to=avatar_path, blank=True, null=True, verbose_name=_("Фото"))
    first_name = models.CharField(max_length=255, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=255, verbose_name=_("Фамилия"))
    firebase_token = models.CharField(blank=True, null=True, max_length=255, verbose_name=_("Токен firebase"))
    role = models.PositiveSmallIntegerField(choices=constants.USER_TYPES, default=0, verbose_name=_("Роль"))
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name=_("Почта"))
    phone = models.CharField(max_length=13, blank=True, null=True, validators=[validate_phone_number],
                             verbose_name=_("Телефон"))
    password_changed_datetime = models.DateTimeField(editable=False, null=True, verbose_name="")
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))
    language = models.CharField(choices=settings.LANGUAGES, max_length=32, default='ru',
                                verbose_name=_("Выбранный язык"))

    USERNAME_FIELD = 'login'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    @property
    def is_staff(self):
        # Anyone who is superuser can enter admin
        return self.is_superuser
