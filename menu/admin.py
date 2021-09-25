from django.contrib import admin
from .models import Subdivision, Employee


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)}
    ordering = ('order',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'subdivision')
    list_filter = ('position',)
    search_fields = ('full_name', 'position')
