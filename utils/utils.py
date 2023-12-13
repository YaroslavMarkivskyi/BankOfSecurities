from .menu import menu

# DataMixin


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        return context
