# Generated by Django 4.2.7 on 2023-11-24 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_billbonds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billbonds',
            old_name='Bonds',
            new_name='bonds',
        ),
    ]