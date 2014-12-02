from django.contrib import admin
from .models import HotelPackage, ExtraPackage, TransferPackage

admin.site.register(HotelPackage)
admin.site.register(ExtraPackage)
admin.site.register(TransferPackage)
