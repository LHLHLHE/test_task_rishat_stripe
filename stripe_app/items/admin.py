from django.contrib import admin

from items.models import Item, Order, OrderItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'price'
    )
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'number',
    )
    search_fields = ('number',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'order_id',
        'item_id',
    )
    search_fields = ('order_id', 'item_id')
