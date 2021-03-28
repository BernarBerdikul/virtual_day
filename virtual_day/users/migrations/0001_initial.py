# Generated by Django 3.1.7 on 2021-03-27 21:52

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import virtual_day.utils.image_utils
import virtual_day.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Время последнего изменения')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='Почта')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=virtual_day.utils.image_utils.avatar_path, verbose_name='Фото')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('firebase_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='Токен firebase')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'STUDENT'), (1, 'ADMIN'), (2, 'MODERATOR'), (3, 'SUPER_ADMIN')], default=0, verbose_name='Роль')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, validators=[virtual_day.utils.validators.validate_phone_number], verbose_name='Телефон')),
                ('password_changed_datetime', models.DateTimeField(editable=False, null=True, verbose_name='Время изменения пароля')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('language', models.CharField(choices=[('ru-RU', 'Russian (Russia)'), ('ru', 'Russian'), ('en', 'English'), ('kk', 'Kazakh'), ('de', 'German')], default='ru', max_length=32, verbose_name='Выбранный язык')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserPushNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Время последнего изменения')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название сообщения')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Текст сообщения')),
                ('image', models.ImageField(blank=True, null=True, upload_to=virtual_day.utils.image_utils.image_push_notification_path, verbose_name='Фото сообщения')),
                ('user_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None, verbose_name='ID-шники пользователей')),
                ('response', models.JSONField(blank=True, default=None, max_length=1000, null=True, verbose_name='Ответ')),
                ('date_publication', models.PositiveIntegerField(blank=True, null=True, verbose_name='Время отправки')),
                ('is_sent', models.BooleanField(blank=True, default=False, null=True, verbose_name='Отправлен')),
                ('users_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Число пользователей')),
                ('data', models.JSONField(blank=True, default=None, max_length=1000, null=True, verbose_name='Данные уведомления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pushes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Шаблон уведомления',
                'verbose_name_plural': 'Шаблоны уведомления',
                'db_table': 'user_push_notification',
            },
        ),
    ]
