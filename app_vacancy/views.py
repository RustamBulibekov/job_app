from django.views.generic import TemplateView


class MainListView(TemplateView):
    template_name = 'main.html'
