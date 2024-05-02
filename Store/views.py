from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Value, F, Func, ExpressionWrapper
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from .models import Collection, Product, Order, OrderItem, Customer

# Create your views here.
def promotion_render(request):
    pass

def collection_render(request):
    pass

def product_render(request):
    #queryset = Product.objects.select_related('collection').all()
    queryset = Order.objects.all()[len(Order.objects.all())-5:]
    products_count = queryset.count()
    mathmatical_operation = OrderItem.objects.filter(product=1).aggregate(num_pro1_sold=Count('id'))
    discount_calc = ExpressionWrapper(F('price')*0.8, output_field=DecimalField())
    annotate_value = Order.objects.annotate(discount_field=discount_calc)
    context = {
        'products': queryset,
        'products_count': products_count,
        'calculation': mathmatical_operation,
        'annotation': annotate_value
    }
   
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
