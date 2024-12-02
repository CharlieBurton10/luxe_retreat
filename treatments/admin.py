from django.contrib import admin
from .models import Treatment, Category

class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'price',
        'time',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Category, CategoryAdmin)