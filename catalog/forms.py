from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(ModelForm, StyleFormMixin):
    class Meta:
        model = Product
        exclude = ('user_owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden_lst = ['casino', 'cryptocurrency', 'crypt', 'stock market', 'cheap', 'free', 'fraud', 'police',
                         'radar']
        for word in forbidden_lst:
            if word in cleaned_data.lower():
                raise ValidationError('Ошибка, связанная с именем продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_lst = ['casino', 'cryptocurrency', 'crypt', 'stock market', 'cheap', 'free', 'fraud', 'police',
                         'radar']
        for word in forbidden_lst:
            if word in cleaned_data.lower():
                raise ValidationError('Ошибка, связанная с описанием продукта')
        return cleaned_data


class ProductModeratorForm(ModelForm, StyleFormMixin):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(ModelForm, StyleFormMixin):
    class Meta:
        model = Version
        fields = "__all__"
