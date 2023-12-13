import requests
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, FormView

from bonds.forms import BondsCreateForm, CurrencyTypeCreateForm, BuyBondsForm
from bonds.models import Bonds
from bonds.services import get_bonds_list, get_bonds, get_payment_table, get_bond_headers, get_payment_days_headers, \
    gen_buy_bonds_trans
from utils.utils import DataMixin


class CurrencyTypeCreateView(DataMixin, CreateView):
    template_name = 'bonds/currency_type_create.html'

    form = CurrencyTypeCreateForm()
    context = {
        'form': form,
    }

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, context=self.context)

    def post(self, *args, **kwargs):
        post_form = CurrencyTypeCreateForm(self.request.POST, self.request.FILES)
        print(post_form)
        if post_form.is_valid():

            post_form.save()
            return redirect('login')
        return render(self.request, self.template_name, context=self.context)


class BondsCreateView(DataMixin, CreateView):
    template_name = 'bonds/bonds_create.html'

    bonds_form = BondsCreateForm()
    context = {
        'form': bonds_form,
    }

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, context=self.context)

    def post(self, *args, **kwargs):
        bonds_form = BondsCreateForm(self.request.POST)
        print(bonds_form)
        if bonds_form.is_valid():
            bonds_form.save()
            return redirect('login')
        return render(self.request, self.template_name, context=self.context)


class BondsMarketView(DataMixin, ListView):
    model = Bonds
    template_name = 'bonds/bonds_list.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ринок")
        context['headers'] = get_bond_headers()
        context['bonds'] = get_bonds_list()
        return dict(list(context.items()) + list(c_def.items()))


class DetailBondsView(DataMixin, DetailView, FormView):
    model = Bonds
    template_name = 'bonds/bonds_detail.html'
    slug_url_kwarg = 'bonds_slug'
    context_object_name = 'bond'
    form_class = BuyBondsForm

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
        return redirect('buy-bonds', bonds=self.kwargs['bonds_slug'])
