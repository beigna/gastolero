from django.db import models


class Transaction(models.Model):
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE,
                                related_name='transactions')

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField()

    description = models.TextField(max_length=100)

    # useful for matching transfers between accounts
    pair = models.ForeignKey('self', on_delete=models.SET_NULL,
                             blank=True, null=True)

    # if this transaction is part of an installment
    installment = models.ForeignKey('installments.Installment',
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)

    def __str__(self):
        return self.description
