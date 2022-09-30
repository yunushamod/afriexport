from django.urls import path, include
from .views import product_detail, product_list
app_name = 'shop'

urlpatterns = [
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('',product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]