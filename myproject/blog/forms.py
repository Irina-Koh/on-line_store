from django.forms import ModelForm, BooleanField
from .models import BlogPost

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

class BlogPostForm(StyleFormMixin, ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('views_counter',)
