from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList
from .models import TrashFile

# Override the base admin template
class CustomAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin Site'

    def each_context(self, request):
        context = super().each_context(request)
        context['my_custom_var'] = 'Hello, world!'
        return context

admin_site = CustomAdminSite(name='customadmin')

class TrashFileAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')

    #set the plural name for this model
    

    def view_on_site(self, obj):
        url = reverse('myapp:view_file', args=[obj.id])
        return format_html('<a href="{}">View on site</a>', url)
    
    def has_add_permission(self, request):
        return False

    change_form_template = 'admin/trashfile_change_form.html'

admin.site.register(TrashFile, TrashFileAdmin)