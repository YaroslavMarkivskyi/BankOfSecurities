from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from depositor.views import *

urlpatterns = [
    path('depositor-create/', DepositorCreateView.as_view(), name='depositor-create'),
]
