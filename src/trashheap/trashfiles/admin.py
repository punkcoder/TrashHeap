from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList
from .models import TrashFile

# Override the base admin template
@admin.register(TrashFile)
class trashfile_admin(admin.ModelAdmin):
    list_display = ('name', 'file', 'file_link', 'file_size', 'file_type', 'file_created', 'file_modified')
    list_filter = ('file_type', 'file_created', 'file_modified')
    search_fields = ('name', 'file')
    readonly_fields = ('file_link', 'file_size', 'file_type', 'file_created', 'file_modified')
    ordering = ('-file_created',)

    def file_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('trashfiles:trashfile_detail', args=[obj.id]), obj.file.name)

    def file_size(self, obj):
        return obj.file.size

    def file_type(self, obj):
        return obj.file.content_type

    def file_created(self, obj):
        return obj.file.created

    def file_modified(self, obj):
        return obj.file.modified

    file_link.short_description = 'File'
    file_size.short_description = 'Size'
    file_type.short_description = 'Type'
    file_created.short_description = 'Created'
    file_modified.short_description = 'Modified'

    # Override the queryset to only show files that are not deleted
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(deleted=False)

    