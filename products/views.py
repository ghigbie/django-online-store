# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse

from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()
    data = {
        "products": list(products.values("pk", "name"))
    }
    response = JsonResponse(data)
    return response


#BELOW IS FOR STANDARD DJANGO PRODUCT
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"