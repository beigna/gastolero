from django.db import models


ACCOUNT_KINDS = (
    ('checking', 'Cuenta Corriente'),
    ('savings', 'Caja de Ahorro'),
    ('credit', 'Tarjeta de Crédito'),
    ('other', 'Otra'),
)


class Account(models.Model):
    bank = models.ForeignKey('banks.Bank', on_delete=models.CASCADE)
    kind = models.CharField(choices=ACCOUNT_KINDS, max_length=20,
                            default='other')

    name = models.CharField(max_length=50)

    number = models.CharField(max_length=50, blank=True, null=True)
    key = models.CharField(max_length=22, blank=True, null=True,
        help_text='CBU/CVU'
    )
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
