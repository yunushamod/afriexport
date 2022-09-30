from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from .forms import CreateProductForm


@login_required
def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CreateProductForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('shop:my_products')
    else:
        form = CreateProductForm()
    return render(request, 'shop/product/create_product.html',{'form': form})


@login_required
def get_my_products(request: HttpRequest, category_slug: str = None) -> HttpResponse:
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(user=request.user)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/my_products.html',{'products': products, 'categories': categories,
    'category': category})


# Create your views here.
@login_required
def product_list(request: HttpRequest, category_slug:str=None) -> HttpResponse:
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).exclude(user=request.user).exclude(quantity=0)
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