from django.http import HttpRequest
from shop.models import Category
from .cart import Cart

def cart(request: HttpRequest):
    categories = Category.objects.all()
    return {'cart': Cart(request), 'categories': categories}