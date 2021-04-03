from django.contrib import admin
from .models import User, UserPushNotification
from ..mixins.paginator import LargeTablePaginator
from ..utils.constants import OBJECTS_PER_PAGE_IN_ADMIN
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ A class used to represent a User model in admin page """
    list_display = ['id', 'email', 'role']
    list_display_links = ['id', 'email', 'role']
    list_filter = ('email',)
    fieldsets = (
        (_('Основные поля'), {'fields': ('email',
                                         'first_name',
                                         'last_name',
                                         'address',
                                         'role',
                                         'phone',
                                         'is_active',
                                         'language')
                              }
         ),
        (_('Пароль'), {'fields': ('password',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2')}
         ),
    )
    ordering = ['email']
    search_fields = ['email']
    list_per_page = OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator


@admin.register(UserPushNotification)
class UserPushNotificationAdmin(admin.ModelAdmin):
    """ A class used to represent a UserPushNotification
        model in admin page """
    list_display = ['id', 'title', 'is_sent', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ('title',)
    fields = ('title', 'description', 'description_detail', 'image',
              'user_ids', 'response', 'date_publication', 'is_sent',
              'users_count', 'views_count', 'data')
    list_per_page = OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator
