from django.urls import path
from catalog.views import products_list, product_detail
from catalog.apps import NewappConfig


app_name = NewappConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
