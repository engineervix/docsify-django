from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    Home Page
    """

    template_name = "home/home.html"
