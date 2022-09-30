from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpRequest, HttpResponse
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.


@login_required
@require_POST
def cart_add(request:  HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override_quantity'])
        return redirect('cart:cart_detail')

@login_required
@require_POST
def cart_remove(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})