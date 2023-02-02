from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "docsify_django.home"
    verbose_name = _("Home")
