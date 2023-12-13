from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CurrencyType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    photo = models.ImageField(upload_to="photos/currencyType/", verbose_name="Фото")

    class Meta:
        verbose_name = 'Тип валюти'
        verbose_name_plural = 'Типи валют'

    def __str__(self):
        return self.name


class Bonds(models.Model):
    YTM = models.BooleanField(verbose_name="Дохід до погашення", default=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Номер", )
    currency_type = models.ForeignKey(CurrencyType, on_delete=models.CASCADE, verbose_name="Тип валюти")
    quantity = models.IntegerField(verbose_name="Кількість", )
    repayment_date = models.DateTimeField(auto_now=False, verbose_name="Дата розміщення")
    denomination = models.DecimalField(verbose_name="Номінал", max_digits=9, decimal_places=2)
    placement_period = models.DateTimeField(auto_now=False, verbose_name="Дата погашення")
    coupon_rate = models.FloatField(verbose_name="Ставка купона", )
    number_payment = models.IntegerField(verbose_name="Кількість виплати купона", default=1,  blank=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Облігації'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.YTM and self.number_payment is None:
            raise ValidationError('Якщо YTM встановлено в True, поле "Кількість виплати купона" обов\'язкове.')
        elif self.YTM is None and self.number_payment:
            raise ValidationError('Якщо YTM встановлено в Fslse, поле "Кількість виплати купона" не обов\'язкове.')

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bonds-detail', kwargs={'bonds_slug': self.slug})

    def __str__(self):
        return self.name
