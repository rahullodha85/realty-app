from django.contrib import admin

from listings.models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date', 'realtor', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'state', 'zip_code', 'description')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)