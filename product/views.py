# from django.shortcuts import render
# from product.models import Product

# # Create your views here.

# def product_list(request):
#     products = Product.objects.all()  
#     return render(request, "product/product_list.html", {"products": products})

from django.views.generic import TemplateView
from .models import Product

class ProductView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_content"] = Product.objects.first() 
        return context
