from django.contrib import admin

# Register your models here.
from .models import StocksSymbolModel

class StocksAdmin(admin.ModelAdmin):

    list_display = ['stock_symbol', 'stock_price']

admin.site.register(StocksSymbolModel, StocksAdmin)
