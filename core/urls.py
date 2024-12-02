from django.urls import path

from .views import (
    index,
    customers,
    order,
    clothes,
    delivery,
    pricing,
    completed,
)

urlpatterns = [
    path('index/', index, name='index',),
    path('customers/', customers, name='customers'),
    path('order/', order, name='order'),
    path('clothes/', clothes, name='clothes'),
    path('delivery/', delivery, name='delivery'),
    path('pricing/', pricing, name='pricing'),
    path('completed/', completed, name='completed'),
]