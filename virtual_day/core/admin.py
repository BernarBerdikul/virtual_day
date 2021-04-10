from django.contrib import admin
from django.utils.safestring import mark_safe
from translations.admin import TranslationInline, TranslatableAdmin
from .models import Billboard, Schedule, StaticBillboard
from django.utils.translation import gettext_lazy as _
from ..mixins.paginator import LargeTablePaginator


@admin.register(StaticBillboard)
class StaticBillboardAdmin(admin.ModelAdmin):
    pass


@admin.register(Billboard)
class BillboardAdmin(TranslatableAdmin):
    """ A class used to represent a Billboard model in admin page """
    list_display = ['id', 'title', 'enable', 'billboard_image']
    list_display_links = ['id', 'title', 'enable', 'billboard_image']
    search_fields = ('title',)
    fields = ('title', 'description', 'type', 'url_link',
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


@admin.register(Schedule)
class ScheduleAdmin(TranslatableAdmin):
    """ A class used to represent a Schedule model in admin page """
    list_display = ['id', 'event', 'speaker_id']
    list_display_links = ['id', 'event', 'speaker_id']
    list_filter = ('period_start', 'period_end')
    fields = ('period_start', 'period_end', 'event', 'billboard',
              'speaker_id',)
    paginator = LargeTablePaginator
    inlines = [TranslationInline]
