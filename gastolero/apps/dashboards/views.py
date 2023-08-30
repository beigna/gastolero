from django.shortcuts import render
from django.utils import timezone

from accounts.models import Account
from transactions.models import Transaction
from transactions.filters import TransactionFilter


def balance(request):
    accounts = Account.objects.all().exclude(kind='credit')

    return render(
        request,
        'dashboards/balance.html',
        {
            'accounts': accounts,
        }
    )


def cards(request):
    accounts = Account.objects.all().filter(kind='credit')

    return render(
        request,
        'dashboards/cards.html',
        {
            'accounts': accounts,
        }
    )


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timezone.timedelta(days=4)
    return next_month - timezone.timedelta(days=next_month.day)


def transactions(request):
    transactions = Transaction.objects.all()

    trans_filter = TransactionFilter(request.GET, queryset=transactions)

    # timestamp based filters
    # timestamp_from = request.GET.get('timestamp_from') or \
    #     timezone.now().replace(day=1).strftime('%Y-%m-%d')
    # timestamp_to = request.GET.get('timestamp_to') or \
    #     last_day_of_month(timezone.now()).strftime('%Y-%m-%d')

    # transactions = transactions.filter(
    #     timestamp__gte=timestamp_from,
    #     timestamp__lte=timestamp_to
    # )

    return render(
        request,
        'dashboards/transactions.html',
        {
            'transactions': trans_filter.qs,
            'filters_form': trans_filter.form,
        }
    )
