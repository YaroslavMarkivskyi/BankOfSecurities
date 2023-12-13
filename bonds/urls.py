from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('bonds-create/', BondsCreateView.as_view(), name='bonds-create'),
    path('currency-type-create/', CurrencyTypeCreateView.as_view(), name='currency-type-create'),
    path('market/bonds/', BondsMarketView.as_view(), name='bonds-list'),
    path('market/bonds/<slug:bonds_slug>/', DetailBondsView.as_view(), name='bonds-detail'),
    # path('logout/', logout_user, name='logout'),
]
