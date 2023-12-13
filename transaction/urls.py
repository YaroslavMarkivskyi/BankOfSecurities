from django.urls import path

from .views import *


urlpatterns = [
    path('market/buy-bonds/<slug:bonds>/', TransactionBuyBondsView.as_view(), name='buy-bonds'),
    path('transaction/sell-bonds/<slug:bonds>/', TransactionSellBondsView.as_view(), name='sell-bonds'),
    path('transaction/history-transaction/', HistoryTransactionView.as_view(), name='history-transaction'),
    path('transaction/history-transaction/<int:pk>/', DetailTransactionView.as_view(), name='detail-transaction'),
]
