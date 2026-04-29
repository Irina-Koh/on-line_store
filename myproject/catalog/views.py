from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products_list.html', context)




def home(request):
    return render(request, 'products/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Данные получены.')
    return render(request, 'products/contacts.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
