# Generated by Django 4.2.7 on 2023-11-25 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0004_alter_bonds_ytm_alter_bonds_denomination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonds',
            name='number_payment',
            field=models.IntegerField(blank=True, default=0, verbose_name='Кількість виплати купона'),
        ),
    ]