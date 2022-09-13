import os
import random

import stripe
from django.db.models import Sum
from django.http import HttpResponseRedirect
from dotenv import load_dotenv
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Item, Order, OrderItem

load_dotenv()

stripe.api_key = os.getenv('STRIPE_API_KEY')


class ItemDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, item_id):
        return Response({'item': get_object_or_404(Item, id=item_id)})


class ListItemAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response({'items': Item.objects.all()})


class BuyItemAPIView(APIView):

    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'{item.name}',
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1/buy_success.html',
            cancel_url='http://127.0.0.1/buy_cancel.html',
        )
        return Response({'id': session.id})


class ListOrdersAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'orders_page.html'

    def get(self, request):
        return Response({'orders': Order.objects.all()})


class OrderDetailAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'order_detail.html'

    def get(self, request, order_id):
        return Response({
            'order': get_object_or_404(Order, id=order_id),
            'order_items': Item.objects.filter(item__order_id=1)
        })


class AddItemToOrderAPIView(APIView):

    def get(self, request, item_id):
        OrderItem.objects.create(
            order=Order.objects.get_or_create(
                id=1,  # 1, т.к. для демонстрации хватит одного заказа
                defaults={'number': random.randint(1111111111, 9999999999)}
            )[0],
            item=Item.objects.get(id=item_id)
        )
        return HttpResponseRedirect('/orders/')


class BuyOrderAPIView(APIView):

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'{order.number}',
                    },
                    'unit_amount': Item.objects.filter(order=order).aggregate(
                        Sum('price')).get('price__sum'),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1/buy_success.html',
            cancel_url='http://127.0.0.1/buy_cancel.html',
        )
        return Response({'id': session.id})
