from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Collection, Product

# Create your views here.
def promotion_render(request):
    pass

def collection_render(request):
    pass

def product_render(request):
    queryset = Product.objects.filter(price__lt=5, inventory__lt=10)
    products_count = queryset.count()
    context = {
        'products': queryset,
        'products_count': products_count,
    }
    print(list(queryset))
    return render(request, 'store/products_list.html', context)

def customer_render(request):
    pass

def order_render(request):
    pass 

def orderitem_render(request):
    pass

def adress_render(request):
    pass

def cart_render(request):
    pass

def cartitem_render(request):
    pass
