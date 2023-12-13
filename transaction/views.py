from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView

from transaction.forms import BuyBondsForm
from transaction.models import Transaction
from transaction.services import buy_bonds_services, sell_bonds_services, get_bargain

from utils.utils import DataMixin


class TransactionBuyBondsView(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'transactions/buy-bonds.html'
    form_class = BuyBondsForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Купити облігації")
        # print(self.request.session.items())
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        code = form.cleaned_data['count']
        session = self.request.session['buy_bonds']
        if code == session['code']:
            buy_bonds_services(session, self.request.user)
            del self.request.session['buy_bonds']
            del self.request.session['attempt']
            return redirect('bonds-list')
        else:
            # print(self.request.session.items())
            self.request.session['attempt'] += 1
            # print(self.request.session['attempt'])
            if self.request.session['attempt'] >= 3:
                del self.request.session['buy_bonds']
                del self.request.session['attempt']
                return redirect('bonds-list')
            else:
                return redirect('buy-bonds', bonds=session['slug'])


class TransactionSellBondsView(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'transactions/sell-bonds.html'
    form_class = BuyBondsForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Продати облігації")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        count = form.cleaned_data['count']
        sell_bonds_services(count, self.request.user, self.kwargs['bonds'])
        return redirect('bonds-list')


class HistoryTransactionView(LoginRequiredMixin, DataMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Історія")
        context['transactions'] = Transaction.objects.all()
        return dict(list(context.items()) + list(c_def.items()))


class DetailTransactionView(LoginRequiredMixin, DataMixin, DetailView):
    model = Transaction
    template_name = 'transactions/detail_transaction.html'
    context_object_name = 'transaction'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"Історія {str(self.object)}")
        context['detail'] = get_bargain(self.object)
        return dict(list(context.items()) + list(c_def.items()))
