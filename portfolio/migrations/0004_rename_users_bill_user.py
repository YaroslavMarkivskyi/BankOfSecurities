# Generated by Django 4.2.7 on 2023-11-21 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_bill_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='users',
            new_name='user',
        ),
    ]