from django.db import models

from accounts.models import User
from bonds.models import Bonds
from utils.transfer_types import TRANSFER_TYPES


class Transaction(models.Model):
    transfer_type = models.CharField(max_length=50, choices=TRANSFER_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Транзакція"
        verbose_name_plural = "Транзакції"

    def __str__(self):
        return self.transfer_type + ' ' + str(self.price) + ' ' + str(self.date)


class Bargain(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    bonds = models.ForeignKey(Bonds, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Кількість")

    class Meta:
        verbose_name = "Угода"
        verbose_name_plural = "Угоди"
