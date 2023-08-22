from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bank', 'kind', 'number', 'key', 'alias')
    list_filter = ('bank', 'kind')
    search_fields = ('name', 'number', 'key', 'alias')
