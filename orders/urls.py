from django.urls import path
from .views import order_create, get_orders

app_name='orders'

urlpatterns = [
    path('create/<int:product_id>/', order_create, name='order_create'),
    path('orders/', get_orders, name='orders'),
]