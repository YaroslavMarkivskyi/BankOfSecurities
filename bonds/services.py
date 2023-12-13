import decimal
import random

from datetime import datetime

from bonds.models import Bonds
from bonds.dto import bonds_model_to_view, payment_table_to_view
from utils.background_transfer import generate_payout_days


def get_bond_headers():
    return {
            'name': 'Назва',
            'currency_type': 'Тип виплати',
            'number_payment': 'Кількість виплат',
            'quantity': 'Кількість',
            'denomination': 'Номінал',
            'coupon_rate': 'Ставка',
            'coupon': 'Купон',
            'repayment_date': 'Дата розміщення',
            'next_payment': 'Дата наступної виплати',
            'placement_period': 'Дата погашення',
            'price': 'Ціна',
    }


def get_payment_days_headers():
    return {
            'name': 'Назва',
            'currency_type': 'Тип виплати',
            'coupon_rate': 'Ставка',
            'coupon': 'Сума виплати',
    }


def get_bonds(bond: Bonds):
    bond_dict = convert_currency_type(bond)
    return bond_dict


def get_bonds_list():
    bonds = Bonds.objects.all()
    bonds_list = []
    for bond in bonds:
        if bond.placement_period.date() > get_current_datetime():
            bond_dict = convert_currency_type(bond)
            bonds_list.append(bond_dict)
    return bonds_list


def convert_currency_type(bond: Bonds):
    if bond.YTM is True:
        price = calc_bonds_price(bond)
        next_payment = get_next_payment(bond)
        coupon = calc_coupon_of_period(bond)
        currency_type = 'YTM'
    else:
        price = calc_bonds_price(bond)
        next_payment = get_next_payment(bond)
        coupon = calc_coupon_of_period(bond)
        currency_type = 'SIM'
    return bonds_model_to_view(bond, price, currency_type, next_payment, coupon)


def calc_bonds_price(bond: Bonds):
    current_datetime = get_current_datetime()
    period = calc_days_of_payment(bond)
    next_payment = get_next_payment(bond)

    ratio = calc_coupon_of_day(bond)
    percent = next_payment - current_datetime
    prev_payment = decimal.Decimal(period - percent.days) * ratio

    price = bond.denomination + prev_payment

    return price


def calc_coupon_of_day(bond: Bonds):
    return bond.denomination * decimal.Decimal(bond.coupon_rate / 100) / decimal.Decimal(365.5)


def calc_days_of_payment(bond: Bonds):
    return (bond.placement_period - bond.repayment_date).days / bond.number_payment


def calc_coupon_of_period(bond: Bonds):
    coupon_of_day = calc_coupon_of_day(bond)
    period = calc_days_of_payment(bond)
    return decimal.Decimal(period) * coupon_of_day


def get_next_payment(bond: Bonds):
    current_datetime = get_current_datetime()
    payout_dates = get_payment_dates(bond)
    next_payment = min([date for date in payout_dates if date > current_datetime])
    return next_payment


def get_current_datetime():
    current_datetime = datetime.now().date()
    # current_datetime = datetime(2023, 9, 8).date()
    return current_datetime


def get_payment_dates(bond: Bonds):
    payout_dates = generate_payout_days(bond.repayment_date, bond.placement_period, bond.number_payment)
    payout_dates.append(bond.repayment_date.date())
    payout_dates.append(bond.placement_period.date())

    return filter_dates(payout_dates)


def get_payment_table(bond: Bonds):
    dates = get_payment_dates(bond)
    dates_list = []
    index = 0
    coupon = calc_coupon_of_period(bond)
    for date in sorted(dates):
        if date != bond.repayment_date.date():
            if date == get_last_date(dates):
                coupon = calc_coupon_of_period(bond) + bond.denomination
            index += 1
            date_dict = payment_table_to_view(index, date, bond.coupon_rate, coupon)
            dates_list.append(date_dict)
    return dates_list


def get_last_date(dates):
    return max(dates)


def filter_dates(dates):
    result = []
    for date in dates:
        if date not in result:
            result.append(date)
    return result


def gen_buy_bonds_trans(slug, count, price):
    return {
        'slug': slug,
        'count': count,
        'price': price,
        'code': generate_trans_code(),
    }


def generate_trans_code():
    code = random.randint(1000, 9999)
    print(code)
    return code
