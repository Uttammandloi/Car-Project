from django.contrib import admin
from .models import car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thubnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10%;" />'.format(object.car_photo.url))

    list_display = ('id', 'car_title', 'thubnail', 'city', 'color', 'model', 'year',
                    'body_style', 'fule_type', 'is_featured',)

    list_display_links = ('id', 'car_title', 'thubnail',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model',
                     'body_style', 'fule_type',)
    list_filter = ('city', 'model', 'body_style', 'fule_type',)


admin.site.register(car, CarAdmin)
