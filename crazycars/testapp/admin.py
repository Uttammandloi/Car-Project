from django.contrib import admin
from .models import team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thubnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 100%;" />'.format(object.photo.url))

    thubnail.short_description = 'photo'

    list_display = ('id', 'thubnail', 'first_name', 'last_name',
                    'designation', 'created_date',)

    list_display_link = ('id', 'thubnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'designation',)
    list_filter = ('designation',)


admin.site.register(team, TeamAdmin,)
