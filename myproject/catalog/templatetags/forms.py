from django.forms import ModelForm

from ..models import Product, Contact, Category



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'