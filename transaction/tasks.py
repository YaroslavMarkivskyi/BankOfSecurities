from celery import shared_task


@shared_task
def process_deposits_task():
    process_deposits()


from celery import shared_task
from decimal import Decimal
from datetime import date, timedelta


@shared_task
def process_deposits():
    pass
    # active_deposits = Deposit.objects.filter(
    #     creation_date__lte=date.today() - timedelta(days=365),
    #     term__gte=(date.today() - F('creation_date')) / timedelta(days=30)
    # )

    # for deposit in active_deposits:
    #     calculate_interest(deposit)


def calculate_interest(deposit):
    interest_rate = 0.05  # Ваша ставка відсотків
    current_date = date.today()

    if current_date >= deposit.creation_date + timedelta(months=deposit.term):
        interest_amount = deposit.amount * Decimal(interest_rate)
        deposit.user.balance += interest_amount
        deposit.user.save()
