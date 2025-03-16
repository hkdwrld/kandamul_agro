from django.views.generic import TemplateView
from .models import AboutUs  # Assuming AboutUs is in the "about" app
from product.models import Product  # Import Product from the products app

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_content"] = AboutUs.objects.first()  # Fetch AboutUs content
        context["products"] = Product.objects.all()  # Fetch all products
        return context
