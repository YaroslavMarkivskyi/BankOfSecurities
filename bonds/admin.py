from django.contrib import admin

from bonds.models import Bonds, CurrencyType

admin.site.register(Bonds)
admin.site.register(CurrencyType)
