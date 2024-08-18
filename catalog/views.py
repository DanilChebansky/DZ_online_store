from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = VersionForm(initial={'product_detail': self.kwargs.get('pk')})
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = VersionForm(initial={'product_detail': self.kwargs.get('pk')})
        return context_data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    # success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])
