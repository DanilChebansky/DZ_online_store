from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data in ['casino', 'cryptocurrency', 'crypt', 'stock market', 'cheap', 'free', 'fraud',
                            'police', 'radar']:
            raise ValidationError('Ошибка, связанная с именем продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data in ['casino', 'cryptocurrency', 'crypt', 'stock market', 'cheap', 'free', 'fraud',
                            'police', 'radar']:
            raise ValidationError('Ошибка, связанная с описанием продукта')
        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
