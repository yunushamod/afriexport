from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm


# Create your views here.
@login_required
def product_list(request: HttpRequest, category_slug:str=None) -> HttpResponse:
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).exclude(quantity=0)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category, 'categories': categories,
        'products': products
    })

@login_required
def product_detail(request: HttpRequest, id: int, slug: str) -> HttpResponse:
    product = get_object_or_404(Product, id = id, slug = slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
    'cart_product_form':  cart_product_form})