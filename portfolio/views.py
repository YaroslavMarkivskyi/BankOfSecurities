from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, FormView

from accounts.models import User
from bonds.models import Bonds
from bonds.services import get_bond_headers, get_payment_days_headers, get_payment_table, gen_buy_bonds_trans
from portfolio.forms import SellBondsForm
from portfolio.models import Bill, BillBonds
from portfolio.services import get_bill_headers, get_bill, get_bonds_headers, get_bonds
from utils.utils import DataMixin


class PortfolioView(DataMixin, DetailView):
    model = User
    template_name = 'portfolio/portfolio_view.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Портфель")
        bill = get_object_or_404(Bill, user=self.request.user)
        context['bill_headers'] = get_bill_headers()
        context['bill'] = get_bill(self.request.user)

        context['bonds_headers'] = get_bonds_headers()
        context['bonds'] = get_bonds(self.request.user)

        return dict(list(context.items()) + list(c_def.items()))


class DetailBondsView(DataMixin, DetailView, FormView):
    model = Bonds
    template_name = 'portfolio/bonds_detail.html'
    slug_url_kwarg = 'bonds_slug'
    context_object_name = 'bond'
    form_class = SellBondsForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(self.object))
        context['bond_headers'] = get_bond_headers()
        context['payment_days_headers'] = get_payment_days_headers()
        context['bond'] = get_bonds(self.object)
        context['payment_days'] = get_payment_table(self.object)

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form, **kwargs):
        count = form.cleaned_data['count']
        slug = form.data['slug']
        price = form.data['price']
        self.request.session['buy_bonds'] = gen_buy_bonds_trans(slug, count, price)
        self.request.session['attempt'] = 0
        return redirect('sell-bonds', bonds=self.kwargs['bonds_slug'])
