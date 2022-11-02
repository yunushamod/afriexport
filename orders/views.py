from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from orders.models import OrderItem
from shop.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created, order_admin_created, order_owner_created

# Create your views here.


def order_create(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    item = cart.get_item(product_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['quantity'])
            cart.remove(product)
            # for item in cart:
            #     product = get_object_or_404(Product, id=item['id'])
            #     OrderItem.objects.create(order=order,
            #     product=product, price=item['price'],
            #     quantity=item['quantity'])
            #cart.clear()
            order_created(order.id)
            order_admin_created(order.id)
            order_owner_created(order.id)
            return render(request, 'orders/order/created.html',
                {'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'item': item, 'form': form})