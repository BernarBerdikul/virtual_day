from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Billboard
from django.utils.translation import gettext_lazy as _


@admin.register(Billboard)
class BillboardAdmin(admin.ModelAdmin):
    """ A class used to represent a Billboard model in admin page """
    list_display = ['id', 'title', 'enable', 'billboard_image']
    list_display_links = ['id', 'title', 'enable', 'billboard_image']
    search_fields = ('title',)
    fields = ('title', 'description', 'url_link', 'enable',
              'billboard_image_in_detail', 'image',
              'type', 'period_start', 'period_end')
    readonly_fields = ('billboard_image_in_detail',)

    def billboard_image_in_detail(self, obj):
        """ function for representing article's image on admin Restaurant change/add page """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="320px" height="240px" />')

    billboard_image_in_detail.short_description = _('Изображение для билборда')
