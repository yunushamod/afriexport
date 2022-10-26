from django.urls import path
from .views import product_detail, product_list, create_product, get_my_products, product_home, search_product
app_name = 'shop'

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('my-products/all/', get_my_products, name="my_products"),
    path('my-products/<slug:category_slug>/', get_my_products, name='my_products_by_category'),
    path('product/search/', search_product, name='search_product'),
    path('', product_home, name='product_home'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('product/list',product_list, name='product_list'),
    path('product/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]