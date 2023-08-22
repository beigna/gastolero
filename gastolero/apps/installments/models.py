from decimal import Decimal

from dateutil.relativedelta import relativedelta

from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.db.models.functions import Coalesce

from transactions.models import Transaction


TWO_PLACES = Decimal('0.01')


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


class Period(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)

    start_at = models.DateField()
    end_at = models.DateField()
    due_at = models.DateField()

    class Meta:
        ordering = ('end_at', )

    @property
    def balance(self):
        qs = self.account.transaction_set.filter(
            timestamp__gte=self.start_at,
            timestamp__lte=self.end_at
        )
        result = qs.aggregate(s=Coalesce(Sum('amount'), 0))['s']
        return Decimal(result).quantize(TWO_PLACES)

    @property
    def is_active(self):
        today = timezone.now().date()
        if today <= self.end_at and today >= self.start_at:
            return True
        return False
