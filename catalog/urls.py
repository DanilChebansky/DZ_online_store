from django.urls import path
from catalog.views import index, contacts, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_detail, name='product_detail')
]
