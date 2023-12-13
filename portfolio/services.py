from django.shortcuts import get_object_or_404

from bonds.services import get_next_payment
from portfolio.dto import bill_model_to_view, bond_model_to_view
from portfolio.models import Bill, BillBonds


def get_bill_headers():
    return {
        'user': 'Користувач',
        'number': 'Номер рахунку',
        'funds': 'Залишок коштів',
        'blocked': 'Заблоковано',
    }


def get_bonds_headers():
    return {
        'index': '№',
        'name': 'ISIN',
        'quantity': 'Кількість',
        'next_payment': 'Дата наступної виплати',
        'placement_period': 'Дата погашення',
    }


def get_bill(user):
    bill = get_object_or_404(Bill, user=user)
    result = bill_model_to_view(bill)
    return result


def get_bonds(user):
    bill = get_object_or_404(Bill, user=user)
    bill_bonds = BillBonds.objects.filter(bill=bill)
    result = []
    index = 0
    for bill_bond in bill_bonds:
        index += 1
        next_payment = get_next_payment(bill_bond.bonds)
        convert = bond_model_to_view(bill_bond, index, next_payment)
        result.append(convert)
    return result
