
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    """
    Render the home page using a class-based view.
    """
    template_name = 'web/index.html'
