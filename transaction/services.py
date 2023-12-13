import decimal

from django.shortcuts import get_object_or_404

from bonds.models import Bonds
from portfolio.models import Bill, BillBonds
from transaction.models import Transaction, Bargain
from utils.transfer_types import BUY, SELL


def convert_str_to_decimal(value):
    result = ''.join(char for char in value if char.isdigit() or char == '.')
    return decimal.Decimal(result)


def buy_bonds_services(session, user):
    bonds_market = get_object_or_404(Bonds, slug=session['slug'])
    user_bill = get_object_or_404(Bill, user=user)
    price = convert_str_to_decimal(session['price']) * session['count']

    if bonds_market.quantity >= session['count'] and user_bill.funds >= price:
        transaction = create_transaction(BUY, user, price)
        create_bargain(transaction, bonds_market, session['count'])
        create_or_update_to_bill_bonds(user_bill, bonds_market, session['count'])

        bonds_market.quantity -= session['count']
        user_bill.funds -= price

        bonds_market.save()
        user_bill.save()
    else:
        raise TypeError()


def sell_bonds_services(count, user, slug):
    bonds_market = get_object_or_404(Bonds, slug=slug)
    user_bill = get_object_or_404(Bill, user=user)
    user_bill_bonds = get_object_or_404(BillBonds, bill=user_bill, bonds=bonds_market)

    if user_bill_bonds.count >= count:
        price = bonds_market.denomination * count

        transaction = create_transaction(SELL, user, price)

        bonds_market.quantity += count
        user_bill.funds += price
        user_bill_bonds.count -= count

        create_bargain(transaction, bonds_market, count)
        user_bill_bonds.save()
        bonds_market.save()
        user_bill.save()
    else:
        raise TypeError()


def create_transaction(transfer_type, user, price):
    transaction = Transaction.objects.create(
        transfer_type=transfer_type,
        user=user,
        price=price,
    )
    return transaction


def create_bargain(transaction, bonds, count):
    Bargain.objects.create(
        transaction=transaction,
        bonds=bonds,
        count=count
    )


def create_or_update_to_bill_bonds(bill, bonds, count):
    bill_bonds, created = BillBonds.objects.get_or_create(
        bill=bill,
        bonds=bonds,
        defaults={'count': count}
    )

    if not created:
        bill_bonds.count += count
        bill_bonds.save()


def get_bargain(transaction):
    bargain = Bargain.objects.filter(transaction=transaction).first()
    if bargain:
        return bargain
    else:
        return ''
