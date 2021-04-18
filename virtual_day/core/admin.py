from django.contrib import admin
from django.utils.safestring import mark_safe
from translations.admin import TranslationInline, TranslatableAdmin
from .models import Billboard, Event, MediaBillboard
from django.utils.translation import gettext_lazy as _
from ..mixins.paginator import LargeTablePaginator


@admin.register(MediaBillboard)
class MediaBillboardAdmin(admin.ModelAdmin):
    pass


@admin.register(Billboard)
class BillboardAdmin(TranslatableAdmin):
    """ A class used to represent a Billboard model in admin page """
    list_display = ['id', 'title', 'enable', 'billboard_image']
    list_display_links = ['id', 'title', 'enable', 'billboard_image']
    search_fields = ('title',)
    fields = ('title', 'description', 'type',
              'billboard_image_in_detail', 'image', 'enable',
              'is_static',)
    readonly_fields = ('billboard_image_in_detail',)
    paginator = LargeTablePaginator
    inlines = [TranslationInline]

    def billboard_image_in_detail(self, obj):
        """ function for representing billboard's
            image on admin change/add page """
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="320px" height="240px" />')

    billboard_image_in_detail.short_description = _('Изображение для билборда')


@admin.register(Event)
class EventAdmin(TranslatableAdmin):
    """ A class used to represent a Event model in admin page """
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    list_filter = ('period_start', 'period_end')
    fields = ('period_start', 'period_end', 'title',)
    paginator = LargeTablePaginator
    inlines = [TranslationInline]
