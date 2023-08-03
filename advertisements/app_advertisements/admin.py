from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'created_date', 'update_date', 'auction']
    list_filter = ['auction', 'created_at']

admin.site.register(Advertisements, AdvertisementsAdmin)


# Register your models here.
