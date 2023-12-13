from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _("Ім'я"),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),)
    first_name = models.CharField(_('Прізвище'), max_length=150)
    last_name = models.CharField(_('По-батькові'), max_length=150)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username', 'last_name']
