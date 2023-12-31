# Generated by Django 4.2.4 on 2023-08-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_account_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
