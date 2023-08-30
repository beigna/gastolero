import django_filters

from django import forms

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    timestamp_from = django_filters.DateFilter(
        field_name='timestamp',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='From',
    )
    timestamp_to = django_filters.DateFilter(
        field_name='timestamp',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='To',
    )

    class Meta:
        model = Transaction
        fields = ['timestamp_from', 'timestamp_to']

    def get_filterset_kwards(self, filterset_class):
        kwargs = super().get_filterset_kwards(filterset_class)

        if kwargs['data'] is None:
            kwargs['queryset'] = kwargs['queryset'].filter(
                timestamp__gte=timezone.now().replace(day=1),
                timestamp__lte=last_day_of_month(timezone.now())
            )

        return kwargs
