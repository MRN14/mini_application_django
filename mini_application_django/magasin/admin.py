from django.contrib import admin

from magasin.models import Product
from magasin.models import Manufacturer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ref', 'name', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer)