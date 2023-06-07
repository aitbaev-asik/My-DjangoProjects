from django.contrib import admin
from .models import Product, Gender, Size, Category, Brand, Contact

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Brand)