from decimal import Decimal
from django.conf import settings
from django.http import HttpRequest
from shop.models import Product
from django.forms.models import model_to_dict

class Cart:
    def __init__(self, request: HttpRequest):
        """
        Initializes the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    def add(self, product: Product, quantity = 1, override_quantity=False):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity']+= quantity
        self.save()
    def save(self):
        """
        Mark the session as "modified" to make sure it gets saved
        """
        self.session.modified = True
    def remove(self, product: Product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        
    def __iter__(self):
        """
        Iterates over the items in the cart and gets the products from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        print(products.values())
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['name'] = product.name
            if(product.image):
                cart[str(product.id)]['image'] = product.image.url
            cart[str(product.id)]['url'] = product.get_absolute_url()
            cart[str(product.id)]['price'] = str(product.price)
            cart[str(product.id)]['id'] = product.id
        for item in cart.values():
            item['price'] = str(item['price'])
            item['total_price'] = str(Decimal(item['price']) * item['quantity'])
            yield item
    def __len__(self):
        """Count all items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())
    def get_total_price(self):
        """
        Gets the total price of all the items in the cart
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self): 
        del self.session[settings.CART_SESSION_ID]
        self.save()
    