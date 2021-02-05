from django.contrib import admin
from .models import User
from ..mixins.paginator import LargeTablePaginator
from ..utils.constants import OBJECTS_PER_PAGE_IN_ADMIN


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ A class used to represent a Manager model in admin page """
    list_display = ['id', 'login', 'email', 'role']
    list_display_links = ['id', 'login', 'email', 'role']
    list_filter = ('login',)
    fieldsets = (
        ('Main Fields', {'fields': ('login',
                                    'email',
                                    'role',)
                         }
         ),
        ('Password', {'fields': ('password',)}),
        ('Permissions', {'fields': ('groups', 'language')}),
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
