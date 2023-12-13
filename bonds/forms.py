# forms.py
from django import forms
from .models import Bonds, CurrencyType


class CurrencyTypeCreateForm(forms.ModelForm):
    class Meta:
        model = CurrencyType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'  # Додає клас 'form-input' для всіх полів
            field.widget.attrs['placeholder'] = field.label  # Встановлює placeholder як ім'я поля


class BondsCreateForm(forms.ModelForm):
    YTM = forms.BooleanField(label="YTM")
    name = forms.CharField(max_length=100)
    currency_type = forms.ModelChoiceField(queryset=CurrencyType.objects.all())
    quantity = forms.IntegerField()
    repayment_date = forms.DateTimeField(input_formats=['%d/%m/%y'])
    denomination = forms.FloatField()
    placement_period = forms.DateTimeField(input_formats=['%d/%m/%y'])
    coupon_rate = forms.FloatField()
    number_payment = forms.IntegerField()

    class Meta:
        model = Bonds
        fields = ['YTM', 'name', 'currency_type', 'quantity', 'repayment_date', 'denomination', 'placement_period',
                  'coupon_rate', 'number_payment']


class BuyBondsForm(forms.Form):
    count = forms.IntegerField(label="Кількість")
