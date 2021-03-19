from django.contrib import admin
from .models import Ice_cream


class Ice_cream_admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'avatar', 'price', 'rating')
    search_fields = ('name',)
    list_filter = ('rating',)
    empty_value_display = 'Пусто'


admin.site.register(Ice_cream, Ice_cream_admin)
