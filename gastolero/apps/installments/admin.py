from django.contrib import admin

from .models import Installment


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'quantity', 'timestamp')
    list_filter = ('account',)
    search_fields = ('account__name', 'description')
