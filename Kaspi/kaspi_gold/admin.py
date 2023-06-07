from django.contrib import admin

from .models import User, Transaction


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'balance', 'phone', 'iin']
    search_fields = ['first_name', 'last_name', 'phone', 'iin']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'sum', 'create_at']
    search_fields = ['sender__first_name', 'recipient__first_name', 'sum']
    list_filter = ['sender', 'recipient']


admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
