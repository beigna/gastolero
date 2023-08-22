from django.shortcuts import render

from accounts.models import Account
from transactions.models import Transaction


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


def transactions(request):
    transactions = Transaction.objects.all()

    return render(
        request,
        'dashboards/balance.html',
        {
            'transactions': transactions,
        }
    )
