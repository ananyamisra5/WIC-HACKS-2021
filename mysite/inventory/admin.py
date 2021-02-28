from django.contrib import admin
from .models import Inventory, Item

class InventoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inventory, InventoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
