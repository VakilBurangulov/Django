from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date','updated_date', 'auction', 'img']
    list_filter = ['auction', 'created_at']

admin.site.register(Advertisements, AdvertisementAdmin)



# Register your models here.