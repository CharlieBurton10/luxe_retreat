from django.contrib import admin
from .models import Membership, Category

class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'description',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Category, CategoryAdmin)