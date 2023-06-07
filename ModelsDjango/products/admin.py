from django.contrib import admin

from .models import Person, Book, Order

admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Order)
