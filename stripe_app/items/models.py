from django.db import models


class Item(models.Model):
    """Модель товаров"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return (
            f'name: {self.name}, '
            f'description: {self.description}, '
            f'price: {self.price}'
        )


class Order(models.Model):
    """Модель заказов"""
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(verbose_name='Номер заказа')
    items = models.ManyToManyField(
        Item,
        through='OrderItem',
        verbose_name='Товары'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'number: {self.number}'


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item')

    class Meta:
        unique_together = ('order', 'item')

    def __str__(self):
        return (
            f'order: {self.order.number}, '
            f'item: {self.item.name}'
        )
