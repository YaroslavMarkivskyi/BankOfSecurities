# Generated by Django 4.2.7 on 2023-11-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='sell_status',
            field=models.BooleanField(default=False),
        ),
    ]
