from django.shortcuts import render, redirect
from django.views.generic import CreateView

from depositor.forms import DepositorCreateForm
from depositor.servises import generate_password


class DepositorCreateView(CreateView):
    template_name = 'depositor/depositor_create.html'

    depositor_form = DepositorCreateForm()
    context = {
        'depositor_form': depositor_form,
    }

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, context=self.context)

    def post(self, *args, **kwargs):
        depositor_form = DepositorCreateForm(self.request.POST)
        if depositor_form.is_valid():
            depositor = depositor_form.save(commit=False)
            hashed_password = generate_password()
            depositor.password = hashed_password
            depositor.save()
            return redirect('login')
        return render(self.request, self.template_name, context=self.context)



