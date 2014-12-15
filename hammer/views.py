from django.views.generic import TemplateView, FormView
from forms import DemoForm

class HomeView(TemplateView):
    template_name = "index.html"


class DemoView(FormView):
    template_name = "forms/demo-form.html"
    form_class = DemoForm