from django.contrib import admin

from realtors.models import Realtor

# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('is_mvp',)
    search_fields = ('name', 'phone', 'email')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)