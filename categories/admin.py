from django.contrib import admin

from categories.models import Category
from product.models import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
