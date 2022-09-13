from django.urls import path

from api.views import ItemDetailAPIView, BuyItemAPIView, ListItemAPIView, \
    OrderDetailAPIView, AddItemToOrderAPIView, BuyOrderAPIView, \
    ListOrdersAPIView

app_name = 'api'

urlpatterns = [
    path('', ListItemAPIView.as_view(), name='index'),
    path('item/<int:item_id>/', ItemDetailAPIView.as_view(), name='item_detail'),
    path('item/<int:item_id>/buy/', BuyItemAPIView.as_view(), name='buy_item'),
    path('orders/', ListOrdersAPIView.as_view(), name='orders'),
    path('orders/<int:order_id>/buy/', BuyOrderAPIView.as_view(), name='buy_order'),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view(), name='order_detail'),
    path('item/<int:item_id>/add-to-order/', AddItemToOrderAPIView.as_view(), name='add_to_order')
]
