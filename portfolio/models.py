import random
import string

from django.db import models
from django.urls import reverse

from accounts.models import User
from bonds.models import Bonds


class Bill(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(verbose_name="Номер рахунку", max_length=50)
    funds = models.DecimalField(verbose_name="Вільні кошти", max_digits=15, decimal_places=2, default=999999999)
    blocked = models.DecimalField(verbose_name="Заблоковані", max_digits=15, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        super(Bill, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Портфель'
        verbose_name_plural = 'Портфелі'


class BillBonds(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    bonds = models.ForeignKey(Bonds, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Кількість")

    def save(self, *args, **kwargs):
        if self.count == 0:
            self.delete()
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Портфель облігацій'
        verbose_name_plural = 'Портфелі облігацій'
