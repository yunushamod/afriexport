from django.http import HttpRequest
from shop.models import Category
from .cart import Cart
from chat.models import Messages

def cart(request: HttpRequest):
    categories = Category.objects.all()
    messages = 0
    if not request.user.is_anonymous:
        messages = Messages.objects.filter(user_to=request.user).exclude(read=True).count()
    return {'cart': Cart(request), 'categories': categories, 'messages': messages}