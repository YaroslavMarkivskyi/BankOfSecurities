# forms.py
from django import forms

from transaction.models import Transaction


class BuyBondsForm(forms.Form):
    count = forms.IntegerField()

    def clean_count(self):
        count = self.cleaned_data['count']
        if count <= 0:
            raise forms.ValidationError("Кількість повинна бути більше нуля.")
        return count
