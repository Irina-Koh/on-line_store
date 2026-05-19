from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm, CharField
from catalog.models import Product, Contact, Category


FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
    'бесплатно', 'обман', 'полиция', 'радар'
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise ValidationError(
                    f'Слово "{word}" запрещено в названии продукта.'
                )
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise ValidationError(
                    f'Слово "{word}" запрещено в описании продукта.'
                )
        return self.cleaned_data['description']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError(
                'Цена не может быть отрицательной.'
            )
        return price

class ContactForm(StyleFormMixin, ModelForm):
    model = Contact
    fields = '__all__'

class CategoryForm(StyleFormMixin, ModelForm):
    model = Category
    fields = '__all__'
