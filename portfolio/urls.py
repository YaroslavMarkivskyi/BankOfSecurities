from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('portfolio/<int:pk>/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/<slug:bonds_slug>/', DetailBondsView.as_view(), name='portfolio-bonds-detail'),
    ]
