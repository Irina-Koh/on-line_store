from catalog.models import Product, Contact
from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'photo', 'category', 'price']
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'photo', 'category', 'price']
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'



