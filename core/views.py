from django.views import generic

class HomeView(generic.TemplateView):
    """
    Website Home page.
    **Template:**
    :template:`core/index.html`
    """
    template_name = "core/index.html"