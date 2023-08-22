from django.contrib import admin

from .models import Installment, Period


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'quantity', 'timestamp')
    list_filter = ('account',)
    search_fields = ('account__name', 'description')


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('account', 'start_at', 'end_at', 'due_at', 'is_active')
    list_filter = ('account',)
    search_fields = ('account__name',)
