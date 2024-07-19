from django.urls import path
from blog.views import RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, \
    RecordDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('blog/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('blog/create', RecordCreateView.as_view(), name='record_create'),
    path('blog/<int:pk>/update', RecordUpdateView.as_view(), name='record_update'),
    path('blog/<int:pk>/delete', RecordDeleteView.as_view(), name='record_delete'),
]
