# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse

from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()
    data = {
         "products": list(products.values())
    }
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'product': {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity
            }
        }
        response = JsonResponse(data)
        return response

    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product does not exist"
            }},
            status=404)
        return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            'manufacturer' : {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_products.values()),
            }
        }
        response = JsonResponse(data)
        return response
    except Manufacturer.DoesNotExist:
        reponse = JsonResponse({
            "error": {
                "code": 404,
                "message:": "Manufacturer not found"
            }},
            status=404)
        return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {
       'manufacturers': list(manufacturers.values())
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