from django.contrib import admin
from .models import Item, Finance

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class FinanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Finance, FinanceAdmin)
