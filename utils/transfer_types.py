SELL = 'SELL'              # ТРАНЗАКЦІЯ ПО ПРОДАЖІ ОБЛІГАЦІЙ
BUY = 'BUY'                # ТРАНЗАКЦІЯ ПО КУПІВЛІ ОЛБІГАЦІЙ
ENROLLMENT = 'ENROLLMENT'  # ТРАНЗАКЦІЯ ПО ЗАРАХУВАННЯ КОШТІВ НА РАХУНОК
DEDUCTION = 'DEDUCTION'    # ТРАНЗАКЦІЯ ПО ВІДРАХУВАННЯ КОШТІВ З РАХУНКУ
PAYOUT = 'PAYOUT'          # ТРАНЗАКЦІЯ ПО ВИПЛАТІ ВІДСОТКІВ З ОБЛІГАЦІЙ


# ТИПИ ТРАНЗАКЦІЙ
TRANSFER_TYPES = ((SELL, SELL), (BUY, BUY), (ENROLLMENT, ENROLLMENT), (DEDUCTION, DEDUCTION), (PAYOUT, PAYOUT))
