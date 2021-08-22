from django.contrib import admin
from .models import Users

admin.site.site_header = "3E DEVELOPMENT API"
admin.site.site_title = "manage api"
admin.site.index_title = "Welcome in Admin panel"


@admin.register(Users)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ('name', 'age')
