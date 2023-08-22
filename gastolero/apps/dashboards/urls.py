from django.urls import path

from .views import (
    balance,
    cards,
    transactions,
)

app_name = 'dashboards'

urlpatterns = [
    path('balance/', balance, name='balance'),
    path('cards/', cards, name='cards'),
    path('transactions/', transactions, name='transactions'),
]
