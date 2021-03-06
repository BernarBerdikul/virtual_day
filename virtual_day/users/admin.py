from django.contrib import admin
from .models import User
from ..mixins.paginator import LargeTablePaginator
from ..utils.constants import OBJECTS_PER_PAGE_IN_ADMIN
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ A class used to represent a User model in admin page """
    list_display = ['id', 'login', 'email', 'role']
    list_display_links = ['id', 'login', 'email', 'role']
    list_filter = ('login',)
    fieldsets = (
        (_('Основные поля'), {'fields': ('login',
                                         'first_name',
                                         'last_name',
                                         'email',
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
            'fields': ('login', 'password1', 'password2')}
         ),
    )
    ordering = ['login']
    search_fields = ['login']
    list_per_page = OBJECTS_PER_PAGE_IN_ADMIN
    paginator = LargeTablePaginator
