from django import forms

from accounts.models import User


class DepositorCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email']


class SellBondsForm(forms.Form):
    count = forms.IntegerField()
