from django.urls import path
from .views import product_detail, product_list, create_product, get_my_products
app_name = 'shop'

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('my-products/all/', get_my_products, name="my_products"),
    path('my-products/<slug:category_slug>/', get_my_products, name='my_products_by_category'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('',product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]