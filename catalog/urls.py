from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactView, CategoryListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/category', CategoryListView.as_view(), name='category_list'),
]
