from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from .forms import CreateProductForm
from django.core.paginator import Paginator


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
def get_my_products(request: HttpRequest, category_slug: str = '') -> HttpResponse:
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
def product_list(request: HttpRequest, category_slug:str='') -> HttpResponse:
    category = None
    categories = Category.objects.all()
    product_list = Product.objects.filter(available=True).exclude(quantity=0)
    #exclude(user=request.user)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = product_list.filter(category=category)
    paginator = Paginator(product_list, 15)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
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


def product_home(request: HttpRequest) -> HttpResponse:
    product_list = Product.objects.filter(available=True).exclude(quantity= 0)
    paginator = Paginator(product_list, 15)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    return render(request, 'shop/product/product_home.html', {
        'products': products,
        'loop_variable': range(products.paginator.num_pages)
    })

def search_product(request: HttpRequest) -> HttpResponse:
    product_name = request.GET.get("search", "")
    if not product_name:
        return redirect('shop:product_list')
    product_list = Product.objects.filter(name__icontains=product_name).exclude(quantity=0)
    paginator = Paginator(product_list, 15)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    return render(request, 'shop/product/search_result.html', {
        'products': products,
        'loop_variable': range(products.paginator.num_pages),
        'search_keyword': product_name
    })