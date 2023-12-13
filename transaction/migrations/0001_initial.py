# Generated by Django 4.2.7 on 2023-11-22 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonds', '0004_alter_bonds_ytm_alter_bonds_denomination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bonds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bonds.bonds')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Транзакція',
                'verbose_name_plural': 'Транзакції',
            },
        ),
    ]