import decimal
from datetime import datetime

from bonds.models import Bonds


def convert_to_decimal(value, symbol='$'):
    return str(decimal.Decimal(value).quantize(decimal.Decimal('0.00'))) + symbol


def convert_to_int(value, symbol=''):
    return str(decimal.Decimal(value).quantize(decimal.Decimal('0'))) + symbol


def convert_to_date(date, symbol=''):
    return str(date.strftime("%d.%m.%Y")) + symbol


def convert_to_str(string, symbol=''):
    return str(string) + symbol


def bonds_model_to_view(bond: Bonds, price, currency_type, next_payment, coupon):
    return {
            'name': convert_to_str(bond.name),
            'currency_type': convert_to_str(currency_type),
            'number_payment': convert_to_int(bond.number_payment),
            'quantity': convert_to_int(bond.quantity),
            'denomination': convert_to_decimal(bond.denomination),
            'coupon_rate': convert_to_decimal(bond.coupon_rate, '%'),
            'coupon': convert_to_decimal(coupon),
            'repayment_date': convert_to_date(bond.repayment_date.date()),
            'next_payment': convert_to_date(next_payment),
            'placement_period': convert_to_date(bond.placement_period),
            'price': convert_to_decimal(price),
            'slug': bond.slug
    }


def payment_table_to_view(index, date, rate, payments):
    return {
        'index': convert_to_int(index),
        'date': convert_to_date(date),
        'rate': convert_to_decimal(rate, '%'),
        'payments': convert_to_decimal(payments),
    }
