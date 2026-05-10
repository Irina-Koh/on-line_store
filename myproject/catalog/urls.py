from django.urls import path
from catalog.apps import NewappConfig
from .views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,ContactListView


app_name = NewappConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/contacts/', ContactListView.as_view(), name='product_contacts')
]
