from datetime import datetime

from django.shortcuts import get_object_or_404


def generate_fake_bonds():
    from faker import Faker
    from datetime import datetime, timedelta

    fake = Faker()

    bonds_list = []

    for _ in range(5):
        bond = {
            "YTM": fake.boolean(),
            "name": fake.uuid4(),  # Генерує випадковий унікальний ідентифікатор
            "currency_type": {"id": fake.random_number(), "name": fake.currency_name()},
            "quantity": 4,
            "repayment_date": datetime(2023, 12, 12),
            "denomination": 1_000,
            "placement_period": datetime(2025, 12, 12),
            "coupon_rate": 20,
            "number_payment": fake.random_number(),
        }
        bonds_list.append(bond)

    return bonds_list


def generate_fake_bills():
    from faker import Faker
    fake = Faker()
    bill_list = []
    for _ in range(5):
        bill = {
            "number": fake.uuid4(),  # Генерує випадковий унікальний ідентифікатор
            "funds": 1_000_000,
            "blocked": 1_000_000,
        }
        bill_list.append(bill)
    return bill_list


def generate_payout_days(last, first, quan):
    lst = []
    per = ((last - first) / quan)
    next_date = first
    for date in range(quan):
        next_date += per
        lst.append(next_date.date())
    return lst


bonds_list = generate_fake_bonds()
bill_list = generate_fake_bills()


#  YTM
# current_datetime = datetime.now().date()
current_datetime = datetime(2024, 6, 11)
for bill in bill_list:
    for bonds in bonds_list:
        if bonds.get('YTM') is True:

            first_date = bonds.get('repayment_date')
            last_date = bonds.get('placement_period')
            quantity = bonds.get('quantity')

            days = generate_payout_days(first_date, last_date, quantity)
            for day in days:
                if day == current_datetime.date():
                    price = ((bonds.get('denomination') / 100) * bonds.get('coupon_rate') * bonds.get('number_payment'))
                    bill['funds'] = price
