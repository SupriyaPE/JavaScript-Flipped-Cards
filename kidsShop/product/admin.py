from django.contrib import admin
from .models import Product,Category,Banner


admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(Product)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "price")