from bonds.dto import convert_to_decimal, convert_to_str, convert_to_date, convert_to_int
from portfolio.models import Bill, BillBonds


def bill_model_to_view(bill: Bill):
    return {
        'user': convert_to_str(bill.user),
        'bill': convert_to_str(bill.number),
        'funds': convert_to_decimal(bill.funds),
        'blocked': convert_to_decimal(bill.blocked)
    }


def bond_model_to_view(bill_bonds: BillBonds, index, next_payment):
    return {
        'index': convert_to_int(index),
        'name': convert_to_str(bill_bonds.bonds),
        'quantity': convert_to_str(bill_bonds.count),
        'next_payment': convert_to_date(next_payment),
        'placement_period': convert_to_date(bill_bonds.bonds.placement_period),
        'slug': bill_bonds.bonds.slug,
    }
