from decimal import Decimal

from dateutil.relativedelta import relativedelta

from django.db import models

from transactions.models import Transaction


class Installment(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    @staticmethod
    def create_transactions(installment):
        amount = installment.amount / Decimal(installment.quantity)

        for i in range(installment.quantity):
            timestamp = installment.timestamp + relativedelta(months=i)

            Transaction.objects.create(
                account=installment.account,
                installment=installment,
                amount=amount,
                timestamp=timestamp,
                description=installment.description,
            )
