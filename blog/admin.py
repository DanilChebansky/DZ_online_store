from django.contrib import admin

from blog.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'views_count', 'slug', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('name', 'created_at',)
